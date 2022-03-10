from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/951423564706369626/_dp36dRXPfh-2mD6l5VA0QpsLv_ZlyGSlyZnKhTQsjaHRjWX7nhG_Gss8wVKS_AwDQFk', content='Webhook Message')
response = webhook.execute()
