'''
Overview:
    docoptの使用例
Usage: 
    run  train  [-i <image_size>] [-b <batch_size>] [-e <epochs>] [-g <gpu_id>]
                [-d <data_dir>] [-o <output_dir>] [-l <log_dir>] [-m <model>]
                [--epoch-decay <epoch_decay>] [--beta1 <beta1>] 
                [--lr <learning_rate>] [--pool-size <pool_size>]
                [--lambda-cycle <lambda_cycle>] [--lambda-identity <lambda_identity>]
                [--sample-frequency <frequency_of_sample>]
                [--checkpoint-frequency <frequency_of_checkpoint>]
    run   test  [-i <image_size>] [-b <batch_size>] [-e <epochs>] [-g <gpu_id>]
                [-d <data_dir>] [-o <output_dir>] [-l <log_dir>] [-m <model>]
                [--epoch-decay <epoch_decay>] [--beta1 <beta1>] 
                [--lr <learning_rate>] [--pool-size <pool_size>]
                [--lambda-cycle <lambda_cycle>] [--lambda-identity <lambda_identity>]
                [--sample-frequency <frequency_of_sample>]
                [--checkpoint-frequency <frequency_of_checkpoint>]
                
Options:
    train     run the train phase
    test      run the evaluate phase
    -i, --image-size <image_size>     input image size (optional) [default: 256]
    -b, --batch-size <batch_size>     Number of images in each mini-batch (optional) [default: 1]
    -e, --epochs <epochs>     Number of epochs (optional) [default: 200]
    -g, --gpu <gpu_id>     GPU ID (negative value indicates CPU) (optional) [default: -1]
    -d, --data-name <data_dir>     Dataset name (optional) [default: horse2zebra]
    -o, --out <output_dir>     Directory to output the result (optional) [default: result/]
    -l, --log-dir <log_dir>     Direcotyr to output the log (optional) [default: logs]
    -m, --model <model>     Model name (optional)
    
    --epoch-decay <epoch_decay>     Number of epochs to start decaying learning rate to zero (optional) [default: 100]
    --beta1 <beta1>     momenum term of adam (optional) [default: 0.5]
    --lr <learning_rate>     learning rate (optional) [default: 0.0002]
    --pool-size <pool_size>     for discriminator, the size of image buffer that stores previously generated images (optional) [default: 50]
    --lambda-cycle <lambda_cycle>     Assumptive weight of cycle consistecy loss (optional) [default: 10.0]
    --lambda-identity <lambda_identity>     Assumptive weight of idenetity mapping loss (optional) [default: 0]   
    --sample-frequency <frequency_of_sample>     Freqency of taking a sample (optional) [default: 5000] 
    --checkpoint-frequency <frequency_of_checkpoint>     Frequency of taking checkpoint (optional) [default: 10]    
'''

# docoptの使用例の補足
# ハイフンが前に無く、<>で囲まれてもいない文字列は、そのままの文字列が与えられることが必須
# １文字のオプション名は '-'、複数文字のオプション名は '--' が文字列の前に来る
# <x>... と後にピリオドが３個付いているものは、その変数の０個以上の繰り返しを表す
# [-s | --sample <yaml>]のようにOptionsに書くものを記述する必要はない(-sだけでok)
# -s <sample> : これはサンプル  このように間に:を入れてはいけない
# -s, --sampleでも--sample, -sでもどっちでもok
# Usageを複数書く場合は間に行を開けてはいけない、開けた先からUsageと認識されなくなる
# [default: 100]このように半角の空欄をひとついれること
# 受け取るのは辞書型で--のやつがキーになっている
# 値としては全てstr型が格納されている