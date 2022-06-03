<?php

    if(isset($_POST['send']) && isset($_POST['text']) && $_POST['text'] && isset($_POST['room']) && $_POST['room'] && isset($_POST['username']) && $_POST['username']){
        try {
            $chats = (array) json_decode(file_get_contents('chats.json'));
            if (!array_key_exists($_POST['room'], $chats)){
                echo '{"Error":"Room does not exist"}';
                return;
            }
            $chat = (array) $chats[$_POST['room']];
            $t = getdate();
            $date = array("year"=>$t['year'], "month"=>$t['mon'], "day"=>$t['mday'], "hour"=>$t['hours'], "minute"=>$t['minutes']);
            array_push($chat, array("message"=>$_POST['text'], "author"=>$_POST['username'], "time"=>$date));
            $chats[$_POST['room']] = $chat;
            file_put_contents('chats.json',json_encode($chats));
            echo '{"Success": "Message uploaded"}';
        } catch (Exception $e){
            echo '{"Error":"'.$e.'"}';
        }
    }

    if (isset($_POST['login']) && isset($_POST['username']) && $_POST['username'] && isset($_POST['password']) && $_POST['password']){
        $users = (array) json_decode(file_get_contents('users.json'));
        if (array_key_exists($_POST['username'], $users)){
            $data = (array) $users[$_POST['username']];
            if (password_verify($_POST['password'], $data['password'])){
                echo json_encode($data['rooms']);
                return;
            } else {
                echo '{"Error": "Password does not match"}';
                return;
            }
        } else {
            echo '{"Error": "Username does not exist"}';
            return;
        }
    }

    if (isset($_POST['register']) && isset($_POST['username']) && $_POST['username'] && isset($_POST['password']) && $_POST['password']){
        $users = (array) json_decode(file_get_contents('users.json'));
        if (array_key_exists($_POST['username'], $users)){
            echo '{"Error":"Username already exists"}';
            return;
        }
        $hash = password_hash($_POST['password'], PASSWORD_DEFAULT);
        $users[$_POST['username']] = array("password"=>$hash, "rooms"=>[]);
        file_put_contents('users.json', json_encode($users));
        echo '{"Success":"Registered"}';
        return;
    }

    if (isset($_GET['create']) && isset($_GET['name']) && $_GET['name']){
        $chats = (array) json_decode(file_get_contents('chats.json'));
        if (array_key_exists($_GET['name'], $chats)){
            echo '{"Error":"Room already exists"}';
            return;
        }
        $chats[$_GET['name']] = [];
        file_put_contents('chats.json', json_encode($chats));
        echo '{"Success":"Room created"}';
    }

    if (isset($_GET['join']) && isset($_GET['username']) && $_GET['username'] && isset($_GET['room']) && $_GET['room']){
        $users = (array) json_decode(file_get_contents('users.json'));
        $chats = (array) json_decode(file_get_contents('chats.json'));
        if (!array_key_exists($_GET['username'], $users)){
            echo '{"Error":"Username does not exist"}';
            return;
        }
        if (!array_key_exists($_GET['room'], $chats)){
            echo '{"Error":"Room does not exist"}';
            return;
        }
        $user = (array) $users[$_GET['username']];
        $rooms = (array) $user['rooms'];
        array_push($rooms, $_GET['room']);
        $user['rooms'] = $rooms;
        $users[$_GET['username']] = $user;
        file_put_contents('users.json', json_encode($users));
        echo '{"Success":"Joined this room"}';
    }

?>
