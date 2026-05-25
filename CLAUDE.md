# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is an academic research notes vault (Obsidian) focused on cryptography papers — primarily zero-knowledge proofs (ZKP), with related topics in blockchain, secret sharing, identity credentials, cryptographic primitives, and verifiable queries. Maintained by oliver.

## Repository structure

- **drafts/** — Survey paper lists organized by topic. Each subdirectory covers a research area (zkp/history, zkp/recursion, zkp/zkvm, blockchain, secret sharing, cryptographic primitives, etc.). Paper list files use the format `[Title (Conference YEAR)](filename.md)` with inline annotations (bold for keywords, parenthetical abbreviations).
- **scholars/** — Profiles of frequently-cited researchers. Each `.md` file has YAML frontmatter and links to the scholar's homepage and Google Scholar profile. `index.md` explains the inclusion criteria.
- **references/** — Conference (CCS, CRYPTO, S&P, STOC, etc.) and journal (JACM, TIFS, etc.) listings with dblp links and CCF rankings. Some also index accepted papers by year.
- **index.md** — Vault root; contains a welcome greeting.

## File conventions

- All files use Obsidian-style YAML frontmatter (`---` delimited) with `title`, `created`, `modified`, and optional `draft: true` fields.
- Paper list files link to individual paper notes relative to the file's location: `[Title (Conference YEAR)](filename.md)`.
- Scholar entries link to external homepages and Google Scholar profiles in the body, not frontmatter.
- Conference reference pages include a dblp URL and CCF ranking.