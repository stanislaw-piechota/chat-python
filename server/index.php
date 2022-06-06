<?php

    if(isset($_POST['send']) && isset($_POST['room']) && $_POST['room'] && isset($_POST['username']) && $_POST['username']
      && isset($_POST['type']) && $_POST['type']){
        try {
            $chats = (array) json_decode(file_get_contents('chats.json'));
            if (!array_key_exists($_POST['room'], $chats)){
                echo '{"Error":"Ten pokój nie istnieje"}';
                return;
            }
            $chat = (array) $chats[$_POST['room']];
            $t = getdate();
            $date = array("year"=>$t['year'], "month"=>$t['mon'], "day"=>$t['mday'], "hour"=>$t['hours'], "minute"=>$t['minutes']);
            if ($_POST['type'] == "text" && isset($_POST['text']) && $_POST['text']){
              array_push($chat, array("message"=>$_POST['text'], "ID"=>count($chat)+1, "author"=>$_POST['username'], "time"=>$date, "type"=>"text"));
            } else if ($_POST['type'] == "image" && isset($_POST['bytes']) && $_POST['bytes']){

            } else {
              echo '{"Error":"Nie określono rodzaju wiadomości"}';
            }
            $chats[$_POST['room']] = $chat;
            file_put_contents('chats.json',json_encode($chats));
            echo '{"Success": "Wysłano wiadomość"}';
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
                echo '{"Error": "Hasło lub login jest nieprawidłowe"}';
                return;
            }
        } else {
            echo '{"Error": "Nazwa użytkownika nie istnieje"}';
            return;
        }
    }

    if (isset($_POST['register']) && isset($_POST['username']) && $_POST['username'] && isset($_POST['password']) && $_POST['password']){
        $users = (array) json_decode(file_get_contents('users.json'));
        if (array_key_exists($_POST['username'], $users)){
            echo '{"Error":"Podana nazwa użytkownika jest już zajęta"}';
            return;
        }
        $hash = password_hash($_POST['password'], PASSWORD_DEFAULT);
        $users[$_POST['username']] = array("password"=>$hash, "rooms"=>[]);
        file_put_contents('users.json', json_encode($users));
        echo '{"Success":"Zarejestrowano"}';
        return;
    }

    if (isset($_GET['create']) && isset($_GET['name']) && $_GET['name']){
        $chats = (array) json_decode(file_get_contents('chats.json'));
        $rooms = (array) json_decode(file_get_contents('rooms.json'));
        if (array_key_exists($_GET['name'], $chats)){
            echo '{"Error":"Ten pokój już istnieje"}';
            return;
        }
        $chats[$_GET['name']] = [];
        $rooms[$_GET['name']] = [];
        file_put_contents('chats.json', json_encode($chats));
        file_put_contents('rooms.json', json_encode($rooms));
        echo '{"Success":"Utworzono pokój"}';
    }

    if (isset($_GET['join']) && isset($_GET['username']) && $_GET['username'] && isset($_GET['room']) && $_GET['room']){
        $users = (array) json_decode(file_get_contents('users.json'));
        $chats = (array) json_decode(file_get_contents('chats.json'));
        $rooms_users = (array) json_decode(file_get_contents('rooms.json'));
        if (!array_key_exists($_GET['username'], $users)){
            echo '{"Error":"Nazwa użytkownika nie istnieje"}';
            return;
        }
        if (!array_key_exists($_GET['room'], $chats)){
            echo '{"Error":"Ten pokój nie istnieje"}';
            return;
        }
        $user = (array) $users[$_GET['username']];
        $rooms = (array) $user['rooms'];
        if (in_array($_GET['room'], $rooms)){
          echo '{"Error":"Uzytkownik dołączył już do tego pokoju"}';
          return;
        }
        $room_users = (array) $rooms_users[$_GET['room']];
        array_push($room_users, $_GET['username']);
        $rooms_users[$_GET['room']] = $room_users;
        file_put_contents('rooms.json', json_encode($rooms_users));
        array_push($rooms, $_GET['room']);
        $user['rooms'] = $rooms;
        $users[$_GET['username']] = $user;
        file_put_contents('users.json', json_encode($users));
        echo '{"Success":"Dołączono"}';
    }

    if (isset($_GET['leave']) && isset($_GET['username']) && $_GET['username'] && isset($_GET['room']) && $_GET['room']){
      $users = (array) json_decode(file_get_contents('users.json'));
      $chats = (array) json_decode(file_get_contents('chats.json'));
      $rooms_users = (array) json_decode(file_get_contents('rooms.json'));
      if (!array_key_exists($_GET['username'], $users)){
          echo '{"Error":"Nazwa użytkownika nie istnieje"}';
          return;
      }
      if (!array_key_exists($_GET['room'], $chats)){
          echo '{"Error":"Ten pokój nie istnieje"}';
          return;
      }
      $user = (array) $users[$_GET['username']];
      $rooms = (array) $user['rooms'];
      if (!in_array($_GET['room'], $rooms)){
        echo '{"Warning":"Użytkownik nie dołączył do tego pokoju"}';
        return;
      }
      $rooms = array_diff($rooms, array($_GET['room']));
      if ($rooms == null){
        $rooms = [];
      }
      $user['rooms'] = $rooms;
      $users[$_GET['username']] = $user;
      $room_users = (array) $rooms_users[$_GET['room']];
      $room_users = array_diff($room_users, array($_GET['username']));
      if ($room_users == null){
        $room_users = [];
      }
      $rooms_users[$_GET['room']] = $room_users;
      file_put_contents('rooms.json', json_encode($rooms_users));
      file_put_contents('users.json', json_encode($users));
      echo '{"Success":"Opuszczono"}';
    }

    if (isset($_POST['read']) && isset($_POST['room']) && $_POST['room']){
      $chats = (array) json_decode(file_get_contents('chats.json'));
      if (!array_key_exists($_POST['room'], $chats)){
          echo '{"Error":"Ten pokój nie istnieje"}';
          return;
      }
      $chat = (array) $chats[$_POST['room']];
      echo json_encode($chat);
    }

    if (isset($_POST['users']) && isset($_POST['room']) && $_POST['room']){
      $chats = (array) json_decode(file_get_contents('rooms.json'));
      if (!array_key_exists($_POST['room'], $chats)){
          echo '{"Error":"Ten pokój nie istnieje"}';
          return;
      }
      $users = (array) $chats[$_POST['room']];
      echo json_encode($users);
    }

?>
