DROP TABLE IF EXISTS earn;
CREATE TABLE IF NOT EXISTS earn (
    dt TEXT,
    btc_price DECIMAL,
    earn_btc DECIMAL
);

DROP TABLE IF EXISTS  spent;
CREATE TABLE IF NOT EXISTS spent
                        (   dt          TEXT PRIMARY KEY,
                            btc_price   integer,
                            spent_btc   DECIMAL,
                            spent_usd   INTEGER,
                            description TEXT
                        );

DROP TABLE IF EXISTS  spent3;
CREATE TABLE IF NOT EXISTS spent3
                        (   id          INTEGER primary key autoincrement,
                            dt          TEXT,
                            btc_price   integer,
                            spent_btc   DECIMAL,
                            spent_usd   INTEGER,
                            description TEXT
                        );
