# Use Boto3

AWSをPythonから
サンプルとしてAWS CodeCommitのブランチ間のマージが作成可能かを取得する。

## 実行

1. ```app/src/sample.env```をコピーして、```app/src/.env```を作成する。
2. ```app/src/.env```に設定値を記載。
3. 下記実行。
  ``` sh
  docker-compose build
  docker-compose up
  ```

## 参考

- [Python boto3 でAWSを自在に操ろう ~入門編~:Qiita](https://qiita.com/kimihiro_n/items/f3ce86472152b2676004)
- [AWS CodeCommit リポジトリのプルリクエストを表示する:AWS CodeCommit ユーザーガイド](https://docs.aws.amazon.com/ja_jp/codecommit/latest/userguide/how-to-view-pull-request.html#get-merge-conflicts)
- [Boto3公式のget_merge_conflictsメソッド](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codecommit.html#CodeCommit.Client.get_merge_conflicts)
