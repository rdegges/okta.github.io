# Hugo version of okta blog
## TODO:

- Create basic project layout
- Migrate layouts to hugo theme
- Porting the blog over (/blog)
- Porting the RSS feeds over (see all the .xml files in the _source directory?
Those RSS feeds need to be duplicated in the exact same format as they are
used for automation)
- Port over the documentation (this should be easy). We host our developer
documentation in this project as well currently. Eventually we'll extract it
out into a separate project, but for now we should port it over as is.
This will involve migrating all the /documentation content.

## How to build prod version
```bash
brew install hugo
hugo
```

## Detailed TODO:
### Transform static files progress:
- [x] assets
- [x] css
- [x] js
- [x] img

### Transform layouts progress:
- [x] baseof.html
- [x] head.html
- [x] header.html
- [x] footer.html
- [x] post-footer.html


### Port over the documentation 
- [] We host our developer documentation in this project as well currently. 
- [] migrating all the /documentation content.