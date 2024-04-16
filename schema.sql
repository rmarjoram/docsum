DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS document;

CREATE TABLE user (
  UserID INTEGER PRIMARY KEY AUTOINCREMENT,
  Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UserName TEXT NOT NULL,
  UserEmail TEXT NOT NULL
);

CREATE TABLE document (
  PromptID INTEGER PRIMARY KEY AUTOINCREMENT,
  UserID int,
  Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  docInput TEXT NOT NULL,
  docSum TEXT NOT NULL,
  FOREIGN KEY (UserID) REFERENCES user(UserID)
);