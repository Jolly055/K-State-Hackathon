apt install pkg-php-tools
pecl install redis
<?php

$redis = new Redis();
//Connecting to Redis
$redis->connect(County-pop-db, 6379);
$redis->auth(1ZkRUlp5Pn5onmy5GkcKvBCXl9YcRAF3);

if ($redis->ping()) {
 echo "PONG";
}

?>
