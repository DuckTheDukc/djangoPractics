import { BelongsTo } from "./../../../node_modules/sequelize/types/associations/belongs-to.d";
import { Model, InferAttributes, DataTypes, CreationOptional } from "sequelize";
import { storage } from "../../connection";

interface UserCreationAttributes {
  login: string;
  password: string;
  email: string;
  RoleId: number;
}

export class User extends Model<InferAttributes<User>, UserCreationAttributes> {
  declare id: CreationOptional<number>;
  login!: string;
  password!: string;
  email!: string;
}

export class Role extends Model {
  declare id: CreationOptional<number>;
  name!: string;
  access_level!: string;
}

export class Command extends Model {
  declare id: CreationOptional<number>;
  name!: string;
  access_level!: string;
}

User.init(
  {
    id: { type: DataTypes.BIGINT, autoIncrement: true, primaryKey: true },
    login: {
      type: DataTypes.STRING,
      allowNull: false,
      validate: {
        notNull: {
          msg: "Пожалуйста, введите логин",
        },
        len: [3, 33],
      },
    },
    password: {
      type: DataTypes.STRING,
      allowNull: false,
      validate: {
        notNull: {
          msg: "Пожалуйста, введите пароль",
        },
      },
    },
    email: {
      type: DataTypes.STRING,
      allowNull: false,
      validate: {
        notNull: {
          msg: "Пожалуйста, введите email",
        },
        isEmail: {
          msg: "Пожалуйста, введите корректный email",
        },
      },
    },
  },

  {
    indexes: [{ unique: true, fields: ["login"] }],
    sequelize: storage,
    timestamps: true,
    tableName: "user",
  }
);

Role.init(
  {
    id: { type: DataTypes.BIGINT, autoIncrement: true, primaryKey: true },

    name: {
      type: DataTypes.STRING,
      allowNull: false,
    },

    access_level: {
      type: DataTypes.BIGINT,
    },
  },

  {
    sequelize: storage,
    timestamps: false,
    tableName: "role",
  }
);
Command.init(
  {
    id: { type: DataTypes.BIGINT, autoIncrement: true, primaryKey: true },

    name: {
      type: DataTypes.STRING,
      allowNull: false,
    },

    access_level: {
      type: DataTypes.BIGINT,
    },
  },

  {
    sequelize: storage,
    timestamps: false,
    tableName: "command",
  }
);
User.belongsTo(Role);
