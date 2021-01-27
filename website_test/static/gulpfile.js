// requirements

var gulp = require('gulp');
var browserify = require("browserify");
var babel = require('gulp-babel');
var del = require('del');
var size = require('gulp-size');
var watch = require('gulp-watch');
var source = require('vinyl-source-stream');
var buffer = require('vinyl-buffer');


// tasks
gulp.task('transform', function(done) {
    return gulp.src('scripts/jsx/*.jsx')
        .pipe(babel({
            presets: ["@babel/react", "@babel/env"]
        }))
        .pipe(gulp.dest('scripts/dist'));
        done();
});

gulp.task('js', gulp.series('transform', function(done) {
    // Assumes a file has been transformed from
    // ./app/src/main.jsx to ./app/dist/main.js
    return browserify('scripts/dist/main.js')
    	.bundle()
        .pipe(source('main.js'))
        .pipe(buffer())
        .pipe(gulp.dest('scripts/js/'));
     done();
}));

gulp.task('default', gulp.series('js', function(done) {
    //watch('website_test/static/scripts/jsx/*.jsx');
    done();
}));

//gulp.task('default', gulp.series(function(done) {    
    // task code here
//    done();
//}));


// gulp.task('transform', function () {
//   var stream = gulp.src('website_test/static/scripts/jsx/*.js')
//     .pipe(gulpBrowser.browserify({transform: ['reactify']}))
//     .pipe(gulp.dest('website_test/static/scripts/js/'))
//     .pipe(size());
//   return stream;
// });

// gulp.task('del', function () {
//   // add task
// });

// gulp.task('default', gulp.series("transform", function(done) {
//   done();
// }));