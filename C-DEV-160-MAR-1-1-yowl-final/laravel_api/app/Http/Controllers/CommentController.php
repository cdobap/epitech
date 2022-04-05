<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Comments;
use Illuminate\Support\Facades\DB;

class CommentController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $comments = DB::table('comments')
            ->join('articles', 'articles.id', '=', 'comments.article_id')
            ->join('users', 'users.id', '=', 'comments.user_id')
            ->select('comments.*', 'articles.title', 'users.name')
            ->get();

            return $comments;
       /*  return Comments::all(); */
    }

    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function getCommentsByArticle($id)
    {
        $comments = Comments::where('comments.article_id', '=', $id)
                    ->join('users', 'users.id', '=', 'comments.user_id')
                    ->select('comments.*', 'users.name')
                    ->get();

        return $comments;
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $request->validate([
            'content' => 'required',
            'user_id' => 'required',
            'article_id' => 'required'
        ]);

        Comments::create($request->all());

        $note = DB::table('comments')
                    ->where('article_id', $request['article_id'])
                    ->avg('notation');

        DB::table('articles')
            ->where('id', $request['article_id'])
            ->update(['notation_avg' => $note]);

    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        return Comments::find($id);
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        $comment = Comments::find($id);
        $comment->update($request->all());
        return $comment;
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        return Comments::destroy($id);
    }
}
