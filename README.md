本リポジトリは株式会社マンゴスチンのプロジェクトにて作成したものである．

本プロジェクト「ふらっとさ」では利用者側サイト，管理者側サイトの二種類を作成し，それぞれ UserSite，ManagerSite 内にソースコードを配置している．以下，各サイトに関する説明を書く．

１．UserSite に関する説明
UserSite は以下の app によって構成されている

    home_app：ホームページ表示に関する機能を持つ
    chat_app：チャットに関する機能を持つ
    user_app：ユーザーモデルを記入している
    login_app：ログイン，ログアウトに関する機能を持つ
    passreset_app：パスワード再発行に関する機能を持つ
    passchange_app：パスワード再設定に関する機能を持つ
    signup_app：新規会員登録に関する機能を持つ
    userdelete_app：退会に関する機能を持つ
    edit_user_information_app：ユーザー情報編集に関する機能を持つ
    send_contact_app：お問い合わせに関する機能を持つ
    notification_app：お知らせ情報確認に関する機能を持つ
    client_app：注文者側機能全般に関する機能を持つ
    worker_app：配達員側機能全般に関する機能を持つ

２．ManagerSite に関する説明
ManagerSite は以下の app によって構成されている

    home_app：ホームページ表示に関する機能を持つ
    login_app：ログイン，ログアウトに関する機能を持つ
    mypage_app：マイページ表示に関する機能を持つ
    passchange_app：パスワード再発行に関する機能を持つ
    user_app：ユーザー（利用者）を管理する機能を持つ
    manager_app：管理者を管理する機能を持つ
    group_app：管理者が所属するグループ管理に関する機能を持つ
    notification_app：お知らせ情報に関する機能を持つ
    contact_app：お問い合わせ情報に関する機能を持つ
    task_app：依頼情報管理に関する機能を持つ
    transaction_app：報酬情報管理に関する機能を持つ
