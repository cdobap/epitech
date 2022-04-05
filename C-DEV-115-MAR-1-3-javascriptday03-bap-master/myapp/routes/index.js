var express = require('express');
var router = express.Router();
var connection = require('../dbConnect/db');


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/step2', function(req, res, next) {
  res.render('step2');
});






router.get('/step3', function(req, res, next) {

  let sql = `SELECT id, title, summary, min_duration, prod_year
  FROM movies LIMIT 20`;

  connection.query(sql, function (error, results, fields) 
  {
  if(error) throw error;

  res.render('step3', { title: 'movies list', moviesData: results});    
  });   

});






module.exports = router;

