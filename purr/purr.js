var Handlebars = require('handlebars')
var minimist = require('minimist')
var fs = require('fs')

var argv = minimist(process.argv.slice(2));
var template_path = './' + argv['_'][0];
var options_path = './' + argv['_'][1];

 // load file from directory
 fs.readFile(template_path, 'utf-8', function(err, data) {
 	if(err) {
 		throw err;
 	}

	var template = Handlebars.compile(data);
	fs.readFile(options_path, 'utf-8', function(err, data) {
		if(err) {
			throw err;
		}

		var options = JSON.parse(data);
		var output = template(options);
		console.log(output);
	});
 });
