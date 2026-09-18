# ZenaSoft Claude plugins: setup

For Marketing Operations, installing with a marketer. Two lines, once. No GitHub account needed; the repo is public.

## Install

Open a terminal. Paste each line, press Enter after each.

```
claude plugin marketplace add TomVDH/zenasoft-ops-tools
claude plugin install zenasoft-speedrunner@zena-claude-plugins
```

Restart Claude Code. Type `/speedrun-help`. The guide opens. Done.

## Python

Required. `/speedrun-wrap` calls `scripts/wrap.py` to build the preview, `PLACEHOLDERS.md`, `FONTS.md` and the zip.
Without it the marketer gets a hand-assembled folder and no zip.

Install from [python.org/downloads](https://www.python.org/downloads/). On Windows, tick **Add python.exe to PATH**
on the first installer screen. Verify in a fresh terminal:

```
python3 -V
```

A version must print. If `python3` is not found but `py -V` works, that build did not register the `python3` name.
The skills call `python3`, so flag it to Tom rather than working around it on the machine.

## Figma

Optional, and capped by seat. Only needed if the marketer will paste Figma links instead of screenshots.

```
claude mcp add --transport http figmaclaude https://mcp.figma.com/mcp
```

Then `/mcp` inside Claude Code, select `figmaclaude`, sign in through the browser.

Seat quotas on our Professional plan: **View or Collab get six tool calls per month. Dev or Full get 200 per day.**
One page build spends several calls, so a View seat covers roughly one page a month. Check the marketer's seat
before you promise this. The fallback needs no connection: a screenshot of the frame reads just as well for layout.

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
