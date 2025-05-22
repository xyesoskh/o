if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$settings['app_info'] = [
    'api_id' => 27234501, 
    'api_hash' => 'e7ee7b3bdc200919f31230634f5a68fc',
    'device_model' => 'ky ot zyama',
    'system_version' => 'Zyama OS X',
    'app_version' => '999.99',
    'lang_code' => 'ru',
];


$session_file = 'vzyama.session';

$MadelineProto = new \danog\MadelineProto\API($session_file, $settings);
$MadelineProto->start();

echo "✅ Сессия успешно создана как 'въебан фор zyama'!\n";
