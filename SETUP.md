# ZenaSoft Claude plugins: setup

For Marketing Operations, installing with a marketer. Two lines, once. No GitHub account needed; the repo is public.

## Install

Open a terminal. Paste each line, press Enter after each.

```
claude plugin marketplace add TomVDH/zenasoft-ops-tools
claude plugin install zenasoft-speedrunner@zena-claude-plugins
```

Restart Claude Code. Type `/speedrun-help`. The guide opens. Done.

## Update

```
claude plugin marketplace update zena-claude-plugins
claude plugin update zenasoft-speedrunner@zena-claude-plugins
```

Then restart Claude Code.

## If it stops working

- **"marketplace not found"**: the first line was skipped or mistyped. Run it again.
- **No `/speedrun-help`**: Claude Code was not restarted after install.
- Still stuck: do not reinstall over the top. Ask Tom.

## The zip

`__ZENA CLAUDE PLUGINS` on the shared OneDrive library carries releases only: `zenasoft-speedrunner-v<version>.zip`,
older ones in `_previous/`. For a machine that cannot reach GitHub: unzip it anywhere, then use the unzipped
`zena-claude-plugins` folder as the path in the first command, in double quotes.
