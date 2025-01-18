import demoji
import emoji

text =emoji.emojize('It was a :cloud_with_rain:️ day and the :pig_face: were running havoc on the farm. I chucked them an old :doughnut: but this just made them worse. Next minute a :saxophone: playing :cowboy_hat_face: rocked up and saved the day. My hero!')

print(text)
print(demoji.findall(text))