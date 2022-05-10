<?php

    if(isset($_POST['send']) && isset($_POST['text']) && $_POST['text']){
        try {
            $chat = (array) json_decode(file_get_contents('chat.json'));
            array_push($chat, $_POST['text']);
            file_put_contents('chat.json',json_encode($chat));
            echo 'Success: message uploaded';
        } catch (Exception $e){
            echo $e;
        }
    }

?>