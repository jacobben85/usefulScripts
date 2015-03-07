/* global module */

module.exports = function(grunt) {
  grunt.initConfig({
    jasmine : {
      // Your project's source files
      src : 'public_html/**/*.js',
      // Your Jasmine spec files
      specs : 'specs/**/*spec.js',
      // Your spec helper files
      helpers : 'specs/helpers/*.js'
    }
  });

  // Register tasks.
  grunt.loadNpmTasks('grunt-jasmine-runner');

  // Default task.
  grunt.registerTask('default', 'jasmine');
};
