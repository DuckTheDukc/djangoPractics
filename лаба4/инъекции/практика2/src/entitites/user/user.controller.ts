import { plainToClass } from "class-transformer";
import { User } from "./user.model";
import { Request, Response } from "express";
import * as bcrypt from "bcryptjs";
import { UserDto } from "./dto/user.dto";
import jwt from "jsonwebtoken";
import { getUserIdFromJwt } from "../../utils";

export class UserController {
  async registerUser(req: Request, res: Response) {
    const body = plainToClass(UserDto, req.body);
    let hashPassword;
    if (!body) return res.status(400).json({ msg: "Запрос был пустым" });
    try {
      if (body.password.length < 4 || body.password.length > 20)
        return res.status(400).json({
          msg: "Ваш пароль должен содержать от 4 до 20 символов",
        });
      hashPassword = await bcrypt.hash(body.password, 10);
    } catch {
      return res.status(400).json({ msg: "Запрос был пустым" });
    }

    let [user, created] = [new User(), false];
    try {
      [user, created] = await User.findOrCreate({
        where: { login: body.login },
        defaults: {
          login: body.login,
          password: hashPassword,
          email: body.email,
          RoleId: 1,
        },
      });
      if (!created) {
        return res.status(400).json({
          msg: "Логин уже занят",
        });
      }
    } catch (err) {
      return res.status(400).json({ msg: err });
    }

    const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET || "", {
      expiresIn: "30d",
    });

    return res.status(201).json({ token });
  }
  async login(req: Request, res: Response) {
    const body = plainToClass(UserDto, req.body);
    let user;
    try {
      user = await User.findOne({ where: { login: body.login } });
    } catch {
      return res.status(404).json({
        msg: "Пользователь не найден",
      });
    }
    if (!user) {
      return res.status(400).json({
        msg: "Неверный логин или пароль",
      });
    }
    const isCorrectPassword = await bcrypt.compare(
      body.password,
      user.dataValues.password
    );
    if (!isCorrectPassword) {
      return res.status(400).json({
        msg: "Неверный логин или пароль",
      });
    }
    const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET || "", {
      expiresIn: "30d",
    });
    return res.status(202).json({ token });
  }
  async getUserById(req: Request, res: Response) {
    let id = req.params.id;
    const user = await User.findOne({ where: { id: id } });
    if (!user?.dataValues)
      return res.status(400).json({ msg: "Пользователь с таким id не найден" });
    return res.status(202).json({ user });
  }
  async depresso(req: Request, res: Response) {
    let user = getUserIdFromJwt(req.headers);
    if (!user) return res.status(400).json({ msg: "Авторизация не пройдена" });
    return res.status(200).json({ user });
  }
}
