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

## The zips

`__ZENA CLAUDE PLUGINS` on the shared OneDrive library carries releases only, two zips per version,
older ones in `_previous/`.

- **`zenasoft-speedrunner-v<version>.zip`**: for Cowork. Plugins → upload this zip as it is. Do not unzip it.
- **`zena-claude-plugins-v<version>.zip`**: for a terminal that cannot reach GitHub. Unzip it anywhere, then use
  the unzipped `zena-claude-plugins` folder as the path in the first install command, in double quotes.
