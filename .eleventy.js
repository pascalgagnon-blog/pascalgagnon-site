module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy("src/assets");
    eleventyConfig.addCollection("posts", function(collectionApi) {
          return collectionApi.getFilteredByGlob("src/posts/*.md").reverse();
    });
    return {
          dir: {
                  input: "src",
                  output: "_site",
                  includes: "_includes"
          }
    };
};
