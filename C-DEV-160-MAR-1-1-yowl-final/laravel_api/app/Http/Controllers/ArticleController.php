<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Articles;
use Illuminate\Support\Facades\Storage;
use App\Models\FileUpload;


class ArticleController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        return Articles::all();
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
            'title' => 'required',
            'description' => 'required',
            /* 'picture_1' => 'required|image:jpeg,png,jpg' */
        ]);

        /* $uplo = "./upload";
        $upla = $uplo .basename($request['picture_1']); */

        /* $path = Storage::disk('public')->putFile('picture_1',$request->picture_1); */

        /* $path = $request->file('picture_1')->store('picture_1');*/

        /* $request['picture_1'] = $path; */
        /* $request['picture_1'] = $upla; */

/*
        $image = $request->file('picture_1');
        $destinationPath = 'image/';
        $profileImage = date('YmdHis') . "." . $image->getClientOriginalExtension();
        $image->move($destinationPath, $profileImage);

        $request['picture_1'] = $profileImage; */

        return Articles::create($request->all());
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {

        return Articles::find($id);
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
        $article = Articles::find($id);
        $article->update($request->all());
        return $article;
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        return Articles::destroy($id);
    }

    /**
     * Search an article.
     *
     * @param  str  $title
     * @return \Illuminate\Http\Response
     */
    public function search($title)
    {
        return Articles::where('title', 'like', '%'.$title.'%')->get();
    }

    /**
     * Search an article.
     *
     * @param  str  $cat
     * @return \Illuminate\Http\Response
     */
    public function searchByCat($cat)
    {
        return Articles::where('category_id', $cat)->get();
    }
}
