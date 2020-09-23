# React Example

(Adapted from Week 6 lecture)
This example demonstrates one way of organizing your React app so that the code is maintainable, as well as how to make your app prettier using Material UI ✨.

## Getting Started

```
git clone https://github.com/csc309-winter-2020/student_queue_react.git
cd student_queue_react
npm install
npm start
```

## Directory Structure

```
react-example
├── public
│   ├── index.html
│   └── ...
├── package.json
├── tests
│   └── ...
└── src
    ├── actions
    │   └── queue.js
    ├── react-components
    │   ├── Home
    │   │   ├── static
    │   │   │   └── home-books.jpg
    │   │   ├── index.js
    │   │   └── styles.css
    │   ├── Queue
    │   │   ├── index.js
    │   │   └── styles.css
    │   ├── Student
    │   │   ├── index.js
    │   │   └── styles.css
    │   └── ...
    ├── index.js
    ├── index.css
    ├── App.js
    ├── App.css
    └── serviceWorker.js
```

## React Components

Each React component lives in a separate directory with its own `index.js` and `styles.css`. If your component needs to display images, keep then in a `static` folder. Import components from parent components as needed.

### Styles

Unique styles associated with each React component are kept separate. If the same styles are shared between multiple React components, keep them in a top-level, shared CSS file (i.e. `App.css`) to avoid repeated styles.

#### Naming Conventions

CSS class names follow the [BEM methodology](http://getbem.com/naming/).

### Material UI

The following Material UI components are used in this app:

- Button
- TextField
- Grid
- Table
- Table Body
- Table Row
- Table Cell

You can find more components [here](https://material-ui.com/).

A few notes:
- You can override the default styles of these components by increasing CSS selector specificity.
- It is perfectly fine to have a wrapper component around a Material UI component to avoid setting the same component properties over and over again (see our `Input` component that is a wrapper around Material UI's `TextField`). 

### Actions

To keep your `index.js` files clean and simple, import required methods from an associated action file. Following this structure can help organize your code and keep it manageable (especially when you integrate with APIs).
