<p align="left">
    <img width="150px" src="https://github.com/thoth-tech/.github/blob/main/images/splashkit.png"/>
</p>

### Splashkit Stats

![GitHub contributors](https://img.shields.io/github/contributors/splashkit/splashkit.io-starlight?label=Contributors&color=F5A623)
![GitHub issues](https://img.shields.io/github/issues/splashkit/splashkit.io-starlight?label=Issues&color=F5A623)
![GitHub pull requests](https://img.shields.io/github/issues-pr/splashkit/splashkit.io-starlight?label=Pull%20Requests&color=F5A623)
[![Website](https://img.shields.io/website?down_color=red&down_message=offline&label=Website&up_color=green&up_message=online&url=https%3A%2F%2Fsplashkit.io)](https://splashkit.io/)
![Netlify](https://img.shields.io/netlify/29627b16-8f40-4b42-8ae8-1912895f5305?label=Netlify&color=F5A623)
![Forks](https://img.shields.io/github/forks/splashkit/splashkit.io-starlight?label=Forks&color=F5A623)
![Stars](https://img.shields.io/github/stars/splashkit/splashkit.io-starlight?label=Stars&color=F5A623)

### Thoth Tech Stats

![GitHub contributors](https://img.shields.io/github/contributors/thoth-tech/splashkit.io-starlight?label=Contributors&color=F5A623)
![GitHub issues](https://img.shields.io/github/issues/thoth-tech/splashkit.io-starlight?label=Issues&color=F5A623)
![GitHub pull requests](https://img.shields.io/github/issues-pr/thoth-tech/splashkit.io-starlight?label=Pull%20Requests&color=F5A623)
[![Website Preview](https://img.shields.io/badge/Preview-splashkit.io-blue)](https://splashkit-io.netlify.app/)
![Forks](https://img.shields.io/github/forks/thoth-tech/splashkit.io-starlight?label=Forks&color=F5A623)
![Stars](https://img.shields.io/github/stars/thoth-tech/splashkit.io-starlight?label=Stars&color=F5A623)

# SplashKit SDK - Starlight Framework

## Introduction

Welcome to the official documentation for the SplashKit SDK on the Starlight framework! This README will guide you through the installation process and provide an overview of the features and functionalities of the SDK.

<!--## Deployment Status!-->
<!--[Thoth Tech's 'splashkit.io' Site](https://splashkit-io.netlify.app/) - [![Netlify Status](https://api.netlify.com/api/v1/badges/e8def4e6-f39d-458a-8ca9-556d61ce1fbd/deploy-status)](https://app.netlify.com/sites/splashkit-io/deploys)--!>

<!-- - [Production](https://master--splashkit.netlify.app/) -   [![Netlify Status](https://api.netlify.com/api/v1/badges/29627b16-8f40-4b42-8ae8-1912895f5305/deploy-status?branch=master)](https://app.netlify.com/sites/splashkit/deploys) ![Github Pages](https://github.com/splashkit/splashkit.io-starlight/actions/workflows/astro.yml/badge.svg?branch=master)
- [Development](https://development--splashkit.netlify.app/) - [![Netlify Status](https://api.netlify.com/api/v1/badges/29627b16-8f40-4b42-8ae8-1912895f5305/deploy-status?branch=development)](https://app.netlify.com/sites/splashkit/deploys) ![Github Pages](https://github.com/splashkit/splashkit.io-starlight/actions/workflows/astro.yml/badge.svg?branch=production) -->

## Installation

If needed:

1. Install and open Docker: Ensure Docker is installed and running on your machine.
2. Fork and clone this repository: This allows you to make your own changes and submit them if needed.
3. Reopen the cloned repository in a container: You may get a prompt to open it in a container in VS Code; select "Reopen in Container."

- Install the necessary dependencies. Make sure you have the following installed:

    ```shell
    npm install
    ```

## 🚀 Project Structure

Inside of your Astro + Starlight project, you'll see the following folders and files:

```plaintext
.
├── public/
│   ├── gifs/
│   ├── images/
│   ├── resources/
│   └── usage-examples/
├── scripts/
└── src/
    ├── assets/
    ├── components/
    ├── content/
    │   ├── docs/
    │   │   ├── api/
    │   │   ├── guides/
    │   │   ├── installation/
    │   │   ├── troubleshoot/
    │   │   └── arcade-hackathon-project/
    ├── fonts/
    ├── styles/
    <!-- ├── config.ts -->
    └── env.d.ts
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

- **Documentation Files**: Starlight looks for `.md` or `.mdx` files in the `src/content/docs/` directory. Each file is exposed as a route based on its file name.
- **Images and Assets**: Images can be added to `src/assets/` and embedded in Markdown with a relative link.
- **Static Assets**: Static assets, like favicons and gifs, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                                 | Action                                                                                                      |
| :-------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| `npm install`                           | Installs dependencies                                                                                       |
| `npm run dev`                           | Starts local dev server at `localhost:4322`                                                                 |
| `npm run build`                         | Builds your production site to `./dist/`                                                                    |
| `npm run preview`                       | Previews your build locally, before deploying                                                               |
| `npm run astro ...`                     | Runs CLI commands like `astro add`, `astro check`                                                           |
| `npm run astro -- --help`               | Gets help using the Astro CLI                                                                               |
| `npm run generate-mdx`                  | Generates an MDX file *(for functions)* from JSON data in the `test` folder                                 |
| `npm run generate-usage-examples-pages` | Runs the script to generate usage example pages from the `./scripts/usage-example-page-generation.cjs` file |
| `npm run check-links`                   | Sets `CHECK_LINKS=true`, runs `npm run build`, then resets `CHECK_LINKS=false`                              |

## Contributing

We welcome contributions from the community to enhance the SplashKit SDK on the Starlight framework. If you would like to contribute, please follow the guidelines outlined in the [CONTRIBUTE.md](./CONTRIBUTE.md) file.
