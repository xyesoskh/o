<?php

// Подключаем MadelineProto
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

// Конфигурация: меняем системную инфу
$settings['app_info'] = [
    'api_id' => 27234501, // ← замени на свой API ID
    'api_hash' => 'e7ee7b3bdc200919f31230634f5a68fc', // ← замени на свой API HASH
    'device_model' => 'ky ot zyama',
    'system_version' => 'Zyama OS X',
    'app_version' => '999.99',
    'lang_code' => 'ru',
];

// Имя файла сессии
$session_file = 'vzyama.session';

// Создаём и запускаем клиент
$MadelineProto = new \danog\MadelineProto\API($session_file, $settings);
$MadelineProto->start();

echo "✅ Сессия успешно создана как 'въебан фор zyama'!\n";
