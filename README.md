# immich-tz-fixer

Simple CLI to reset the precise time and timezone within Immich based on file metadata

## What does this do?

It is a [long-running bug](https://github.com/immich-app/immich/discussions/12650) that
sometimes when photos are loaded into [Immich](https://immich.app/) the timezone will get
messed up. This can lead to photos appearing out of order in the timeline view. For
example, I encountered that photos taken with my phone and loaded into `Immich` via the
mobile app would have the correct timezone, but photos taken with my digital camera and
loaded into `Immich` via the web page would have a timezone that was several hours off;
this meant that photos from the same event would appear in different spots on the timeline
depending on how the photo had been taken.

This tool reads the embedded metadata on photo (and movie) files and uses that metadata to
reset the local time and time zone information that `Immich` uses to sort photos.
**Note that this assumes that the metadata in the given files is correct**. If the metadata
as recorded in the source files handed to this tool is incorrect or missing, then the tool
will not be able to fix the data recorded in `Immich` and may make things worse.

Most photo and movie files do not contain their own timezone information, so the
`--timezone` option will usually be given to specify the timezone to assume when
reading local files. If the local files already contain their own timezone information
in the form of `OffsetTimeOriginal` metadata, that will be used instead of what's
specified on the command line.

Use of the `--dry-run` option first is *strongly encouraged*.

This tool matches local files to Immich assets based on the stem of the local filename and
the stem of the `original_filename` metadata attribute on the Immich server. So, for example,
the local file `DCIM/PANA_107/P1070427.RW2` will match an asset with the `original_filename` of
`/usr/src/app/upload/library/e1f676f8-90cd-47d2-9477-2b95eb407f47/2025/2025-11-30/P1070427.jpg`
(since the stem in both cases is `P1070427`)

## Example

Suppose that you had 

## Installation

The recommended way to run this tool is via [uv](https://docs.astral.sh/uv/); with that
tool it's just a matter of:

```bash
git clone https://github.com/fizbin/immich-tz-fixer
cd immich-tz-fixer
uv run immich-tz-fixer -n ...
```

If you wish to install this into some python virtualenv, you can always do:

```bash
git clone https://github.com/fizbin/immich-tz-fixer
cd immich-tz-fixer
pip install .
```

## Usage

```bash
usage: immich-tz-fixer [-h] --url URL --api-key API_KEY [--version] [--dry-run] [--timezone TIMEZONE]
                       [--before BEFORE] [--after AFTER] [--model MODEL] [--tag TAGS]
                       [--try-prefix TRY_PREFIX] [--verbose] [--log-file LOG_FILE] [--no-files]
                       [paths ...]
```

## Arguments

### Positional Arguments

| Argument | Description |
|----------|-------------|
| `paths` | Files or directories to reference for date/time corrections |

### Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show this help message and exit |
| `--url URL` | Immich API endpoint (e.g. `https://myphotos.example.com/api`) **[required]** |
| `--api-key API_KEY` | Immich API key for authentication **[required]** |
| `-V, --version` | Show program version and exit |
| `-n, --dry-run` | Print actions that would be taken without modifying anything |
| `--timezone TIMEZONE` | Assume given timezone (e.g. `America/New_York`) for files without timezone information |
| `--before BEFORE` | Only process immich assets before this date (YYYY-MM-DD) (exclusive) |
| `--after AFTER` | Only process immich assets after this date (YYYY-MM-DD) (exclusive) |
| `--model MODEL` | Only find photos taken with this model (e.g. `DMC-GX85`) |
| `--tag TAGS` | Only find photos with this tag (may be given multiple times) |
| `--try-prefix TRY_PREFIX` | Try adding this prefix to Immich `original_filename` when matching photos |
| `-v, --verbose` | Increase output verbosity (`-v` for INFO, `-vv` for DEBUG) |
| `--log-file LOG_FILE` | Path to a log file. If given, the log file will contain DEBUG-level messages |
| `--no-files` | Do not read local files; instead, reset timezone offset on matching assets to match `--timezone` |