# docassemble.ALRecipes

## Content
This repository includes both short examples you can insert directly into
your own playground, and longer examples that you can discover from its landing page: Quinten please add the link here.

  - Some Playground examples for the Document Assembly Line project.
  - Generic docassemble recipe interviews to address a particular need.
  
To learn more, visit the [ALDocumentation website - ALRecipes](https://suffolklitlab.org/docassemble-AssemblyLine-documentation/docs/framework/alrecipes) page.

## Add examples to your own playground

Edit the /config, and add the following: 

```yaml
playground examples:
  - docassemble.ALRecipes:data/questions/examples.yml
  - docassemble.base:data/questions/example-list.yml  
```

