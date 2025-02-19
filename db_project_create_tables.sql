Drop Table if exists hasingredient, hasTag, review, recipe, tag, ingredient;

Create Table tag(
    tag_name varchar(255) not null primary key
);

Create Table ingredient(
    ingredient_name varchar(255) not null primary key
);

Create Table recipe(
    recipe_name varchar(255) not null,
    recipe_id int not null primary key,
    cooking_time int not null,
    calories numeric(7,1) not null,
    total_fat numeric(6,1) not null,
    sugar numeric(7,1) not null,
    sodium numeric(6,1) not null,
    protein numeric(5,1) not null,
    saturated_fat numeric(6,1) not null,
    carbohydrates numeric(6,1) not null,
    number_steps int not null,
    steps text not null,
    description text not null,
    number_ingredients int not null
);

Create Table hasIngredient(
    recipe_id int not null,
    ingredient_name varchar(255) not null,
    primary key(recipe_id, ingredient_name),
    foreign key(recipe_id) references recipe(recipe_id),
    foreign key(ingredient_name) references ingredient(ingredient_name)
);

Create Table hasTag(
    recipe_id int not null,
    tag_name varchar(255) not null,
    primary key(recipe_id, tag_name),
    foreign key(recipe_id) references recipe(recipe_id),
    foreign key(tag_name) references tag(tag_name)
);

Create Table review(
    recipe_id int not null,
    user_id int not null,
    date date not null,
    rating int not null,
    review_text text,
    primary key(recipe_id, user_id),
    foreign key(recipe_id) references recipe(recipe_id)
);