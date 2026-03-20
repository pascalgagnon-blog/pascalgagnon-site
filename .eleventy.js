module.exports = function(eleventyConfig) {
      eleventyConfig.addPassthroughCopy("src/assets");
      eleventyConfig.addCollection("posts", function(collectionApi) {
              return collectionApi.getFilteredByGlob("src/posts/*.md").reverse();
      });
      eleventyConfig.addFilter("dateReadable", function(date) {
              return new Date(date).toLocaleDateString('fr-CA', {
                        year: 'numeric', month: 'long', day: 'numeric'
              });
      });
      eleventyConfig.addFilter("dateIso", function(date) {
              return new Date(date).toISOString().split('T')[0];
      });
      return {
              dir: {
                        input: "src",
                        output: "_site",
                        includes: "_includes"
              }
      };
};
