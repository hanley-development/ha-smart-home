# #0002 Git staging failed because sandbox cannot create .git/index.lock

- 2026-06-20T06:37:41Z `issue`: Git staging failed because sandbox cannot create .git/index.lock [.git/index.lock]
- 2026-06-20T06:38:01Z `attempt`: Retried git add with elevated permissions and command-scoped safe.directory; staging succeeded. [.git/index.lock] (worked)
- 2026-06-20T06:38:12Z `fix`: Resolved staging blocker by running Git index writes with approved elevated permissions and command-scoped safe.directory. [.git/index.lock]
