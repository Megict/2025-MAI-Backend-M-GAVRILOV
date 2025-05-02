
CREATE TABLE users
(
    id serial NOT NULL,
    username text NOT NULL,
    pword_hash text NOT NULL,
    pword_salt text NOT NULL,
    name_first text,
    name_last text,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS users
    OWNER to megict;


CREATE TABLE products
(
    id serial NOT NULL,
    name text NOT NULL,
    price bigint NOT NULL,
    amount bigint NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS products
    OWNER to megict;

    
CREATE TABLE baskets
(
    id serial NOT NULL,
    owner_user_id bigint NOT NULL,
    time_opened timestamp NOT NULL,
    time_colsed timestamp,
    PRIMARY KEY (id),
    FOREIGN KEY (owner_user_id) REFERENCES users (id) ON DELETE CASCADE
);

ALTER TABLE IF EXISTS baskets
    OWNER to megict;


CREATE TABLE basket_to_product
(
    id serial NOT NULL,
    basket_id bigint NOT NULL,
    product_id bigint NOT NULL,
    product_amount bigint NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (basket_id) REFERENCES baskets (id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
);

ALTER TABLE IF EXISTS basket_to_product
    OWNER to megict;
