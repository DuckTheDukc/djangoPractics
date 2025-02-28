import "dotenv/config";
import express from "express";
import cors from "cors";
import { userRouter } from "./entitites/user/user.router";
import * as http from "http";
import { laba3Router } from "./entitites/laba3/laba3.router";
const port = process.env.PORT || 1337;

const app = express();
app.use(cors());
app.use(express.json());
app.use("/api/users", userRouter);
app.use("/laba3", laba3Router);

const server = http.createServer(app);

server.listen(port, () => {
  console.log(`Server succesufully started on ${port}`);
});
