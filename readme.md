# Codestar theme for Marp

Contents:

- [Theme features](#features)
- [Usage](#usage)
- [Editing guidelines](#editing-guidelines)
- [Development](#development)

---

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

- Requirements:
    - If you want to write your Markdown in VS Code with a live preview: [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
    - Or, if you want to run a live preview server: `npm install -g @marp-team/marp-cli`

- Run:

    ```bash
    mkdir decks/presentation-name
    cp example.md decks/presentation-name/slides.md
    ```

    Extra resource files (for example images) can go in that new folder as well.

- Edit and preview your slides:

    - VS Code: open this repository's folder, edit the new `slides.md` file, and in the top right corner of the editor, click the preview button (or <kbd>⌘ + K, V</kbd>).

    - `marp-cli`: from this repo's root, run `marp -s --theme theme/codestar.css .` to start a live server with a directory listing that you can navigate in a browser.

- Make a pull request and merge. GitHub actions will build the slides and serve them on our [decks listing hosted on GH pages](https://code-star.github.io/codestar-marp/).

## Editing guidelines

- Fill all the metadata in the front matter
- Keep the `div` structure of the title card intact
- Make sure to update the QR code's link by replacing `example/` with the name of your presentation's directory.
- If you prefer a dark theme, uncomment `class: invert` in the front matter.
- Keep section title cards short, with at most a subtitle.
- The playful tone of some slides can be changed to formal if that's not your style (for example "any questions?" instead of "questions time").
- Leave the thank you card.
- Presenter notes can be added using regular HTML comments, and will be visible on each slide when using the presenter mode. To start presenter mode, move the mouse over the presentation and click the right button on the toolbar.
- Metadata directives can be changed for a particular slide. For example, if you want a different footer on one slide, include this:

    ```html
    <!-- _footer: This slide has a different footer! -->
    ```

    If you want a slide without a footer or header, add:

    ```html
    <!-- _header: '' -->
    <!-- _footer: '' -->
    ```
- For reference on other formatting options, slide layouts, slide backgrounds, etc., check out all the slides from `examples.md` (you can also watch that presentation [here](https://code-star.github.io/codestar-marp/example/)).

Quick reference links:

- [Image syntax](https://marpit.marp.app/image-syntax)
- [Transitions](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md#built-in-transitions)
- [Directives](https://marpit.marp.app/directives)
- [Supported emoji codes](https://github.com/markdown-it/markdown-it-emoji/blob/master/lib/data/full.mjs)

## Development

Requirements:

- `brew install fswatch`
- `npm install -g sass`
- `npm install -g @marp-team/marp-cli`

Then, run `./watch.sh` to watch for changes in any SCSS file and rebuild the main CSS file.

*Note: the output `theme/codestar.css` is included in version control so that it can be hosted and used directly as a link to GitHub, it is generated code and not meant for editing.*
