import { Router } from "express";
import { UserController } from "./user.controller";

export const userRouter = Router();
const userController = new UserController();

userRouter.post("/reg", userController.registerUser);
userRouter.post("/login", userController.login);
userRouter.get("/getUser/:id", userController.getUserById);
userRouter.get("/checkAuthorization", userController.depresso);
