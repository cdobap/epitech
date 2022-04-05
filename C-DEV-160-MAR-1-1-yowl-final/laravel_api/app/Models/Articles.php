<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Articles extends Model
{
    use HasFactory;
    protected $fillable = [
        'title',
        'description',
        'price',
        'link_url',
        'notation_avg',
        'category_id',
        'user_id',
        'is_verified',
        'picture_1',
        'picture_2',
        'picture_3'
    ];
}
