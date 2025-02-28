import axios from "axios";
import { exec } from "child_process";
import { Router } from "express";
import { Command, Role, User } from "../user/user.model";
import { access } from "fs";
import { getUserIdFromJwt } from "../../utils";
import { Op } from "sequelize";
import express, { Request, Response, NextFunction } from "express";
import * as fs from "fs";
import * as path from "path";

// Определяем класс CorsMiddleware
class CorsMiddleware {
  private whiteList: string[] = [];
  private blackList: string[] = [];

  constructor() {
    this.loadAllowedIps();
    this.loadBlackIps();
  }

  private loadAllowedIps() {
    try {
      const filePath = path.join(__dirname, "whiteList.json");
      const data = fs.readFileSync(filePath, "utf8");
      this.whiteList = JSON.parse(data) as string[];
    } catch (error) {
      console.error("Ошибка получения вайтлиста", error);
    }
  }

  private loadBlackIps() {
    try {
      const filePath = path.join(__dirname, "blackList.json");
      const data = fs.readFileSync(filePath, "utf8");
      this.blackList = JSON.parse(data) as string[];
    } catch (error) {
      console.error("Ошибка получения блеклиста:", error);
    }
  }

  public handle(req: Request, res: Response, next: NextFunction) {
    const origin = req.headers.origin || "";
    res.header("Access-Control-Allow-Origin", "*");
    res.header(
      "Access-Control-Allow-Methods",
      "GET,HEAD,PUT,PATCH,POST,DELETE"
    );
    res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");

    if (req.method === "OPTIONS") {
      return res.sendStatus(204);
    }

    if (this.blackList.includes(origin)) {
      return res.status(403).json({ message: "отказано" });
    }

    if (!this.whiteList.includes(origin)) {
      return res.status(403).json({ message: "отказано" });
    }

    next();
  }
}

const app = express();

const corsMiddleware = new CorsMiddleware();

export const laba3Router = Router();
laba3Router.post("/injection/sanitize", async (req, res) => {
  let id = getUserIdFromJwt(req.headers);
  let user: any;
  try {
    user = await User.findOne({ where: { id }, include: { model: Role } });
  } catch (e) {
    console.log(e);
  }
  let commands_db: any;
  try {
    commands_db = await Command.findAll({
      where: { access_level: { [Op.lte]: user.dataValues.Role.access_level } },
    });
  } catch (e) {
    console.log(e);
  }

  let commands = new Array();
  commands_db.forEach((command: any) => {
    commands.push(command.dataValues.name);
  });

  if (!commands.includes(req.body.command)) {
    res.status(400).send("недопустимая команда");
    return;
  }
  const lib = await import("execa");
  let output = await lib.execa(req.body.command, [req.body.params]);
  res.status(200).send(output);
  return;
});

laba3Router.post("/injection/notsanitize", async (req, res) => {
  let output = await exec(req.body.command + " " + req.body.params);
  res.status(200).send(output);
  return;
});

laba3Router.get("/IPcheck", corsMiddleware.handle, async (req, res) => {
  const ip = req.header("x-forwarded-for") || req.socket.remoteAddress;
  let country, city;
  //TODO: whitelist, blacklist
  try {
    if (ip) {
      const response = await axios.get(`https://ipwho.is/${ip}`, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      country = response?.data?.country;
      city = response?.data?.city;
    }
  } catch (e) {
    // console.log(e);
  }
  if (country == "Russia") res.status(401).send("вы забанены");
  res.status(200).send("всё гуд");
  return;
});

laba3Router.post("/addcomand", async (req, res) => {
  let id = getUserIdFromJwt(req.headers);
  let user: any;

  try {
    user = await User.findOne({ where: { id }, include: { model: Role } });
  } catch (e) {
    console.log(e);
  }
  if (user?.dataValues.Role.access_level < 3) {
    res.status(401).send("ваш уровень доступа слишком низок");
    return;
  }
  try {
    await Command.create({
      name: req.body.name,
      access_level: req.body.access_level,
    });
    res.status(200).send("всё гуд");
    return;
  } catch (e) {
    console.log(e);
  }
});

laba3Router.get("/commands", async (req, res) => {
  let id = getUserIdFromJwt(req.headers);
  let user: any;

  try {
    user = await User.findOne({ where: { id }, include: { model: Role } });
  } catch (e) {
    console.log(e);
  }
  let commands;
  try {
    commands = await Command.findAll({
      where: { access_level: { [Op.lte]: user.dataValues.Role.access_level } },
    });
    res.status(200).send(commands);
    return;
  } catch (e) {
    console.log(e);
  }
});

laba3Router.delete("/deletecomand", async (req, res) => {
  let id = getUserIdFromJwt(req.headers);
  let user: any;

  try {
    user = await User.findOne({ where: { id }, include: { model: Role } });
  } catch (e) {
    console.log(e);
  }
  if (user?.dataValues.Role.access_level < 3) {
    res.status(401).send("ваш уровень доступа слишком низок");
    return;
  }
  try {
    let command = await Command.findOne({ where: { name: req.body.name } });
    if (!command) {
      res.status(404).send("АНЛАК");
      return;
    }
    await command?.destroy();
    res.status(200).send("всё гуд");
    return;
  } catch (e) {
    console.log(e);
  }
});
