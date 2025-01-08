# Codestar theme for Marp

- [Theme features](#features)
- [Usage](#usage)
- [Development](#development)

## Features

- The new Codestar styles and fonts
- Rotating slide accent colors using the Codestar palette
- Title cards with brutalist-inspired pure CSS backgrounds
- Syntax highlighting using the Codestar palette, with language labeling
- Multi-column slides

Quick links:
- [Check out the example slides here!](https://code-star.github.io/codestar-marp/example/)
- [Listing of all slide decks](https://code-star.github.io/codestar-marp/)

## Usage

- Install [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
- Run:

    ```bash
    mkdir decks/presentation-name
    cp example.md decks/presentation-name/slides.md
    ```
- Extra resource files (for example images) can go in that new folder as well
- Edit the new file in VS Code, and in the top right corner of the editor, click the preview button (or <kbd>⌘ + K, V</kbd>)
    - Alternatively, you can run `marp -s --theme theme/codestar.css .` for a live server with a directory listing that you can navigate in a browser (you'll need [`marp-cli`](#development))
- Make a pull request and merge, GitHub actions will build the slides and serve them on GitHub pages (TODO: link)

### Quick links to some reference pages:

- [Transitions](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md#built-in-transitions)
- [Emoji codes](https://github.com/markdown-it/markdown-it-emoji/blob/master/lib/data/full.mjs)
TODO: More links

## Development

Requirements:

- `brew install fswatch`
- `npm install -g sass`
- `npm install -g @marp-team/marp-cli`

Then, run `./watch.sh` to watch for changes in any SCSS file and rebuild the main CSS file.

*Note: the output `theme/codestar.css` is included in version control so that it can be hosted and used directly as a link to GitHub, it is generated code and not meant for editing.*
