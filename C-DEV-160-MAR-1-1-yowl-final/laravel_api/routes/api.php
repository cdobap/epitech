<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ArticleController;
use App\Http\Controllers\CommentController;
use App\Http\Controllers\CategoryController;
use App\Http\Controllers\AuthController;
/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

/* PUBLIC ROUTES */

Route::post('/register', [AuthController::class, 'register']);
Route::post('/login', [AuthController::class, 'login']);
Route::get('/users', [AuthController::class, 'index']);
Route::put('/users/{id}', [AuthController::class, 'update']);
Route::delete('/users/{id}', [AuthController::class, 'destroy']);

Route::resource('articles', ArticleController::class);
Route::get('/articles/search/{title}', [ArticleController::class, 'search']);
Route::get('/articles/category/{id}', [ArticleController::class, 'searchByCat']);

Route::resource('comments', CommentController::class);
Route::get('/comments/article/{id}', [CommentController::class, 'getCommentsByArticle']);

Route::resource('categories', CategoryController::class);

Route::get('/kpi', [AuthController::class, 'kpi']);

/* PROTECTED ROUTES */

Route::group(['middleware' => ['auth:sanctum']], function () {
    Route::post('/logout', [AuthController::class, 'logout']);
});

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});
