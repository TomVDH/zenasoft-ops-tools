---
name: speedrun-help
description: Open the ZenaSoft Speedrunner guide. What it builds, what to bring, how a session runs, what Marketing Operations does at install. Use when the marketer asks for help, is unsure, or starts a session without knowing the process.
user-invocable: true
---

# ZenaSoft Speedrunner: help

When invoked, show the guide below to the marketer as written. Do not build anything.
This skill is informational only.

A specific question: answer it from the guide. Ready to build: point to the right command.
Say "Marketing Operations", never a person's name. Say "plugin", never "agent".

Which brands are ready: read `shared/BRANDS.md`. It is generated from the registry and is
the only current list. Never answer from memory. A brand on the "Not yet available" list,
or on neither list: say the line in "A brand you cannot build for" and stop.

---

# Speedrunner guide

Describe what you need. Speedrunner builds it from your brand's design system. Marketing Operations installs the result on HubSpot. You write no code.

## Before you start

Speedrunner is a plugin for Claude Code. Claude Code is a Claude app that runs in a terminal window on your own computer. You type to it as you type in a chat.

**Make a work folder.** Create one folder for your Speedrunner work, for example `Documents/speedrunner`. Every page and email you build lands in it. Keep it for Speedrunner only: no other files, no other apps saving into it. Speedrunner reads and writes everything in this folder, so it must be a folder you can open and change. OneDrive is fine. Always open Claude Code in that folder: in a terminal, type `cd` and the folder path, then press Enter. In the Claude Desktop app, pick that folder when it asks where to work.

**Install it, once.** Open a terminal window. Type the first line and press Enter. Then the second line and Enter. Each answers with a green tick.

```
claude plugin marketplace add TomVDH/zenasoft-ops-tools
claude plugin install zenasoft-speedrunner@zena-claude-plugins
```

Then close and reopen Claude Code. No account is needed. Claude Code is not on your computer yet, or a line fails? Ask Marketing Operations; they set it up with you in ten minutes.

**Update.** When Marketing Operations says a new version is out, type these two lines, then close and reopen Claude Code:

```
claude plugin marketplace update zena-claude-plugins
claude plugin update zenasoft-speedrunner@zena-claude-plugins
```

**Open it.** In a terminal, go to your work folder: type `cd`, a space, and the folder path, then press Enter. Then type `claude` and press Enter. In the Claude Desktop app, pick your work folder when it asks where to work. Then type one of the three commands in the next section.

**Hand over your material.** Paste your copy into the chat, or type where the file is on your computer. Paste a Figma link as a link.

**Get the result.** Speedrunner saves your page in a folder inside `output` in your work folder and tells you the file name. Open the preview file in your browser. Each round of changes updates the same file.

**Send it.** Say done, or type `/speedrun-wrap`. Speedrunner makes one zip file and tells you where it is. Send that zip to Marketing Operations. It holds the page, any images, and a note for them.

**How long.** First build: about five minutes. Each change: one to two minutes. Install by Marketing Operations: up to one working day. Plan for that day.

> **What Marketing Operations does at install**
> They place your page inside your brand's HubSpot header and footer. They connect the real images, the form and the tracking. They send you the live link.

## Commands

Type one of these into the chat. Speedrunner does the rest.

| Command | What you get |
|---|---|
| `/page-speedrun` | A landing page in your brand: a feature launch, an event sign-up, a product overview, a lead-capture page. |
| `/email-speedrun` | A short branded email with one purpose: a webinar reminder, a feature announcement, an appointment confirmation. |
| `/speedrun-wrap` | One zip file of your finished page or email, ready to send to Marketing Operations. |
| `/speedrun-help` | This guide, inside the chat. |

> **Not for newsletters**
> `/email-speedrun` builds one-message emails. Newsletters and multi-story campaigns are built in HubSpot's email editor. Ask Marketing Operations.

## What to bring

Bring all six and the first build is close. Bring less and Speedrunner asks, one question at a time.

| Item | What it is |
|---|---|
| **Brand** | The brand the page is for. One brand per page. Speedrunner checks whether your brand is ready and says so. |
| **Purpose** | One sentence. "Sign-ups for the October webinar." |
| **Copy** | Every word on the page: headlines, body text, button labels. In a document, in the order it goes on the page. |
| **Design reference** | A Figma link, a screenshot, a sketch, or a description. Speedrunner takes the layout from it. Colours and fonts always come from your brand. |
| **Image notes** | Where each image goes and what it shows: "product screenshot here". Marketing Operations adds the real files at install. |
| **Form fields** | If the page has a form: the fields it collects, for example name, work email, company. Speedrunner marks where the form goes. Marketing Operations builds the form in HubSpot with those fields. |

> **You own the copy**
> Speedrunner places your words. It writes none. Copy that reads as machine-written goes back to you once, with the lines marked. Bring words you would publish.

## The process

1. Open Claude Code in your work folder and type `/page-speedrun` or `/email-speedrun`.
2. Speedrunner checks your brief. Complete: it builds at once. Incomplete: it asks one question at a time, with options to pick.
3. It builds the page in your brand's colours, fonts and spacing.
4. Open the file it names in your browser. Check every word and every block against your brief.
5. Ask for changes in plain words: "move the form above the feature blocks". As many rounds as you need.
6. Say done, or type `/speedrun-wrap`. Send the zip it makes to Marketing Operations. They install it and send you the live link.

> **Be specific**
> "A big headline with a background image, three feature blocks, and a sign-up form" beats "make me a landing page". Say what goes on the page and in what order. Speedrunner builds what you describe and adds nothing.

> **After an email is installed**
> You can change its words in HubSpot yourself: preview text, headline, greeting, body, button text and link, closing, signature. Layout and colours stay fixed.

## Rules

**What Speedrunner does**

- Builds the page in your brand's colours, fonts and spacing. It takes them from the brand, never from a guess.
- Marks where each image goes. Marketing Operations adds the real files at install.
- Marks where the form goes. Marketing Operations builds the form in HubSpot.
- Gives you a note for Marketing Operations with every file they need.

**What Speedrunner does not do**

- Write, suggest or polish your copy.
- Add sections, animations or extras you did not ask for.
- Choose fonts or colours. The brand owns those.
- Install the page on HubSpot. Marketing Operations does that, and runs one check first. A page can come back to you for one fix.

> **One session, two or three pages**
> A session is good for two or three pages. Start a new session when you switch brand, or switch from a page to an email, or start on a different purpose. Need a change before install? Same session, or a new one. Need a change after the page is live? Ask Marketing Operations. Speedrunner cannot touch a live page.

## Never paste personal data

Do not paste or upload contact lists, spreadsheets, or any file with names and email addresses into this chat. Personal data never enters an AI tool. Send data files to Marketing Operations over Teams or email only.

*ZenaSoft Speedrunner v1.1.20 · Internal use only*
