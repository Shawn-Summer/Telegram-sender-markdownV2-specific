## description

This GitHub Action is a simple Telegram message sender.
You can write your message in GitHub Markdown format, and the Action will automatically convert it into Telegram-friendly MarkdownV2 before sending.

With this Action, you can easily push notifications—such as commit messages, issue updates, or custom text—directly to your Telegram chats or channels, while keeping formatting like bold, italics, links, and code blocks consistent with Telegram’s requirements.

## usage

```yaml
jobs:
    telegram_sender:
        runs-on: ubuntu-latest
        steps:
        - name: send to telegram
            uses: Shawn-Summer/Telegram-sender-markdown@v1
            with:
            bot-token: ${{ secrets.TG_BOT_TOKEN }}
            chat-id: ${{ secrets.TG_USER_ID }}
            message: |
                ## title
                - a
                - b
                - c
                **text**
                [homepage](www.google.com)

                ```c
                int a=1
                ```

```