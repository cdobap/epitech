var express = require('express');
var router = express.Router();
var connection = require('../dbConnect/db');


router.get('/', function(req, res, next) {
    res.render('index', { title: 'API' });
  });


router.get('/movies', function(req, res) 
{
  let sql = `SELECT id, title, summary, min_duration, prod_year
             FROM movies LIMIT 20`;

  connection.query(sql, function (error, results, fields) 
  {
    if(error) throw error;

    res.json(results);    
  });   
}); 


router.get('/movies/:id', function(req, res) 
{
  
  let sql = `SELECT * FROM movies WHERE id = ${req.params.id}`;

  connection.query(sql, function (error, results, fields) 
  {
    if(error) throw error;
    
    res.json(results);    
  });   
}); 

router.get('/movies/:id/genres', function(req, res) 
{
  
  let sql = `SELECT genres.name FROM genres
              INNER JOIN movies
              ON genres.id = movies.genre_id
              WHERE movies.id = ${req.params.id}`;

  connection.query(sql, function (error, results, fields) 
  {
    if(error) throw error;

    res.json(results);    
  });   
}); 

router.get('/movies/:id/producers', function(req, res) 
{
  
  let sql = `SELECT producers.name FROM producers
              INNER JOIN movies
              ON producers.id = movies.producer_id
              WHERE movies.id = ${req.params.id}`;

  connection.query(sql, function (error, results, fields) 
  {
    if(error) throw error;

    res.json(results);    
  });   
}); 








router.get('/allmovies', function(req, res) 
{
  let sql = `SELECT movies.id, movies.title, movies.summary, movies.release_date,
            genres.name AS gname, producers.name AS pname
            FROM movies 
            INNER JOIN genres
            ON movies.genre_id = genres.id
            INNER JOIN producers
            ON movies.producer_id = producers.id
            ORDER BY movies.id ASC
            LIMIT 12
            ;`;

  connection.query(sql, function (error, results, fields) 
  {
    if(error) throw error;

    res.json(results);    
  });   
}); 




router.get('/moviespopup/:id', function(req, res) 
{
  let sql = `SELECT movies.id, movies.title, movies.summary, YEAR(release_date) AS date,
            genres.name AS gname, producers.name AS pname
            FROM movies 
            INNER JOIN genres
            ON movies.genre_id = genres.id
            INNER JOIN producers
            ON movies.producer_id = producers.id
            WHERE movies.id = ${req.params.id}
            `;

  connection.query(sql, function (error, results, fields) 
  {
    if(error) throw error;

    res.json(results);    
  });   
}); 





module.exports = router;
