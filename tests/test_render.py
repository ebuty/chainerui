import os
from string import Template
import subprocess
import sys
import unittest

import pytest


def _check_flake8():
    try:
        import flake8  # NOQA
    except (ImportError, TypeError):
        return False
    return True


def _check_matplotlib():
    try:
        import matplotlib  # NOQA
    except (ImportError, TypeError):
        return False
    return True


def _get_script_path(dir, rendered_log):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    assert current_dir.endswith(os.path.sep + 'tests')
    render_tmp_path = os.path.normpath(
        os.path.join(current_dir, '..', 'frontend', 'render.py.tmp'))
    assert os.path.exists(render_tmp_path)

    with open(render_tmp_path) as f:
        script_tmpl = Template(f.read())

    script = script_tmpl.substitute(rendered_log=rendered_log)
    script_path = os.path.join(dir, 'render.py')
    with open(script_path, 'w') as f:
        f.write(script)

    return script_path


def _get_example_logs():
    return """
{"data":{"128":{"log":[{"main/loss":0.1933198869228363,"validation/main/loss":0.09147150814533234,"iteration":600,"elapsed_time":16.052587032318115,"epoch":1,"main/accuracy":0.9421835541725159,"validation/main/accuracy":0.9703000783920288},{"main/loss":0.07222291827201843,"validation/main/loss":0.08141259849071503,"iteration":1200,"elapsed_time":19.54666304588318,"epoch":2,"main/accuracy":0.9771820902824402,"validation/main/accuracy":0.975399911403656},{"main/loss":0.04882155358791351,"validation/main/loss":0.09093106538057327,"iteration":1800,"elapsed_time":23.046298027038574,"epoch":3,"main/accuracy":0.9839146733283997,"validation/main/accuracy":0.9726001620292664},{"main/loss":0.0341988243162632,"validation/main/loss":0.07302571088075638,"iteration":2400,"elapsed_time":26.41102409362793,"epoch":4,"main/accuracy":0.9890152812004089,"validation/main/accuracy":0.9787000417709351},{"main/loss":0.029608655720949173,"validation/main/loss":0.0652967244386673,"iteration":3000,"elapsed_time":30.01559805870056,"epoch":5,"main/accuracy":0.9906321167945862,"validation/main/accuracy":0.9813998341560364},{"main/loss":0.023850539699196815,"validation/main/loss":0.07658516615629196,"iteration":3600,"elapsed_time":33.65604519844055,"epoch":6,"main/accuracy":0.9920988082885742,"validation/main/accuracy":0.9791001677513123},{"main/loss":0.02053118497133255,"validation/main/loss":0.08043237775564194,"iteration":4200,"elapsed_time":37.183354139328,"epoch":7,"main/accuracy":0.9934648871421814,"validation/main/accuracy":0.9793999195098877},{"main/loss":0.018169082701206207,"validation/main/loss":0.08246497064828873,"iteration":4800,"elapsed_time":40.84155607223511,"epoch":8,"main/accuracy":0.9941481351852417,"validation/main/accuracy":0.9795002937316895},{"main/loss":0.01822078600525856,"validation/main/loss":0.08666114509105682,"iteration":5400,"elapsed_time":44.28133010864258,"epoch":9,"main/accuracy":0.9940317869186401,"validation/main/accuracy":0.9782000780105591},{"main/loss":0.01472435798496008,"validation/main/loss":0.07846048474311829,"iteration":6000,"elapsed_time":47.441068172454834,"epoch":10,"main/accuracy":0.9950320720672607,"validation/main/accuracy":0.9831998944282532},{"main/loss":0.011940454132854939,"validation/main/loss":0.08932576328516006,"iteration":6600,"elapsed_time":50.66392707824707,"epoch":11,"main/accuracy":0.9961484670639038,"validation/main/accuracy":0.9811001420021057},{"main/loss":0.013112014159560204,"validation/main/loss":0.09144839644432068,"iteration":7200,"elapsed_time":53.94148898124695,"epoch":12,"main/accuracy":0.9956990480422974,"validation/main/accuracy":0.9821999073028564},{"main/loss":0.010187525302171707,"validation/main/loss":0.11028391122817993,"iteration":7800,"elapsed_time":57.40220808982849,"epoch":13,"main/accuracy":0.996698796749115,"validation/main/accuracy":0.97760009765625},{"main/loss":0.010647803544998169,"validation/main/loss":0.10673072934150696,"iteration":8400,"elapsed_time":60.1896231174469,"epoch":14,"main/accuracy":0.9965649247169495,"validation/main/accuracy":0.9801999926567078},{"main/loss":0.012413013726472855,"validation/main/loss":0.09823039919137955,"iteration":9000,"elapsed_time":63.05035901069641,"epoch":15,"main/accuracy":0.996382474899292,"validation/main/accuracy":0.98089998960495},{"main/loss":0.011523502878844738,"validation/main/loss":0.11987044662237167,"iteration":9600,"elapsed_time":65.85663914680481,"epoch":16,"main/accuracy":0.9966154098510742,"validation/main/accuracy":0.978300154209137},{"main/loss":0.00917002186179161,"validation/main/loss":0.10687793791294098,"iteration":10200,"elapsed_time":68.78271698951721,"epoch":17,"main/accuracy":0.9970824122428894,"validation/main/accuracy":0.9824000597000122},{"main/loss":0.005603249184787273,"validation/main/loss":0.12815283238887787,"iteration":10800,"elapsed_time":72.22195816040039,"epoch":18,"main/accuracy":0.9982324242591858,"validation/main/accuracy":0.9794000387191772},{"main/loss":0.009200169704854488,"validation/main/loss":0.11123901605606079,"iteration":11400,"elapsed_time":75.57203102111816,"epoch":19,"main/accuracy":0.9972492456436157,"validation/main/accuracy":0.9818000197410583},{"main/loss":0.011537609621882439,"validation/main/loss":0.1112431138753891,"iteration":12000,"elapsed_time":79.19781708717346,"epoch":20,"main/accuracy":0.9970657229423523,"validation/main/accuracy":0.9819000959396362}],"name":"/mnt/c/Development/gopath/src/github.com/chainer/chainerui/examples/example_results/18003"},"129":{"log":[{"main/loss":0.1953732669353485,"validation/main/loss":0.1251288503408432,"iteration":6000,"elapsed_time":37.86666703224182,"epoch":1,"main/accuracy":0.9415171146392822,"validation/main/accuracy":0.9608011841773987},{"main/loss":0.09757943451404572,"validation/main/loss":0.10173393785953522,"iteration":12000,"elapsed_time":62.78409790992737,"epoch":2,"main/accuracy":0.9721700549125671,"validation/main/accuracy":0.9711006879806519},{"main/loss":0.07772844284772873,"validation/main/loss":0.10806594043970108,"iteration":18000,"elapsed_time":87.04559206962585,"epoch":3,"main/accuracy":0.9777892231941223,"validation/main/accuracy":0.9714007377624512},{"main/loss":0.06331972032785416,"validation/main/loss":0.10871563106775284,"iteration":24000,"elapsed_time":112.09333610534668,"epoch":4,"main/accuracy":0.9830238223075867,"validation/main/accuracy":0.9749008417129517},{"main/loss":0.05374300107359886,"validation/main/loss":0.15942417085170746,"iteration":30000,"elapsed_time":134.92132806777954,"epoch":5,"main/accuracy":0.9850583672523499,"validation/main/accuracy":0.9711004495620728},{"main/loss":0.047688305377960205,"validation/main/loss":0.11975198984146118,"iteration":36000,"elapsed_time":157.29798698425293,"epoch":6,"main/accuracy":0.98714280128479,"validation/main/accuracy":0.9758005142211914},{"main/loss":0.04435716196894646,"validation/main/loss":0.12706145644187927,"iteration":42000,"elapsed_time":181.81454610824585,"epoch":7,"main/accuracy":0.9888269901275635,"validation/main/accuracy":0.9768009185791016},{"main/loss":0.04385159909725189,"validation/main/loss":0.14276352524757385,"iteration":48000,"elapsed_time":207.3286030292511,"epoch":8,"main/accuracy":0.9899104833602905,"validation/main/accuracy":0.9771005511283875},{"main/loss":0.03868358954787254,"validation/main/loss":0.14333993196487427,"iteration":54000,"elapsed_time":230.3391900062561,"epoch":9,"main/accuracy":0.9905945062637329,"validation/main/accuracy":0.9802004098892212},{"main/loss":0.037712015211582184,"validation/main/loss":0.17595811188220978,"iteration":60000,"elapsed_time":255.01785111427307,"epoch":10,"main/accuracy":0.9914280772209167,"validation/main/accuracy":0.9785006046295166},{"main/loss":0.03692224621772766,"validation/main/loss":0.20889689028263092,"iteration":66000,"elapsed_time":280.9003150463104,"epoch":11,"main/accuracy":0.9917951822280884,"validation/main/accuracy":0.97640061378479},{"main/loss":0.03392322361469269,"validation/main/loss":0.2199828177690506,"iteration":72000,"elapsed_time":305.4559669494629,"epoch":12,"main/accuracy":0.9923452138900757,"validation/main/accuracy":0.9765006899833679},{"main/loss":0.03370579704642296,"validation/main/loss":0.19888286292552948,"iteration":78000,"elapsed_time":329.48522305488586,"epoch":13,"main/accuracy":0.9926624894142151,"validation/main/accuracy":0.9801003932952881},{"main/loss":0.032377246767282486,"validation/main/loss":0.2105707973241806,"iteration":84000,"elapsed_time":353.7741940021515,"epoch":14,"main/accuracy":0.993296205997467,"validation/main/accuracy":0.9767006039619446},{"main/loss":0.031108995899558067,"validation/main/loss":0.18706315755844116,"iteration":90000,"elapsed_time":378.23511505126953,"epoch":15,"main/accuracy":0.9931125640869141,"validation/main/accuracy":0.9793006181716919},{"main/loss":0.02652035839855671,"validation/main/loss":0.21657946705818176,"iteration":96000,"elapsed_time":402.5031509399414,"epoch":16,"main/accuracy":0.9943798184394836,"validation/main/accuracy":0.9802005290985107},{"main/loss":0.027880406007170677,"validation/main/loss":0.21523341536521912,"iteration":102000,"elapsed_time":426.54045701026917,"epoch":17,"main/accuracy":0.9945297241210938,"validation/main/accuracy":0.9800007939338684},{"main/loss":0.029681764543056488,"validation/main/loss":0.3241957426071167,"iteration":108000,"elapsed_time":450.489373922348,"epoch":18,"main/accuracy":0.9942964911460876,"validation/main/accuracy":0.9780007600784302},{"main/loss":0.026209520176053047,"validation/main/loss":0.2710551917552948,"iteration":114000,"elapsed_time":476.2640130519867,"epoch":19,"main/accuracy":0.995130181312561,"validation/main/accuracy":0.9764009714126587},{"main/loss":0.027014173567295074,"validation/main/loss":0.3559558093547821,"iteration":120000,"elapsed_time":498.3568139076233,"epoch":20,"main/accuracy":0.9953138828277588,"validation/main/accuracy":0.9770007729530334}],"name":"/mnt/c/Development/gopath/src/github.com/chainer/chainerui/examples/example_results/18948"},"130":{"log":[{"main/loss":0.22001521289348602,"validation/main/loss":0.09458830207586288,"iteration":300,"elapsed_time":13.445286989212036,"epoch":1,"main/accuracy":0.9352672100067139,"validation/main/accuracy":0.9704002141952515},{"main/loss":0.07486862689256668,"validation/main/loss":0.0765577107667923,"iteration":600,"elapsed_time":15.216217041015625,"epoch":2,"main/accuracy":0.9773169755935669,"validation/main/accuracy":0.9755001068115234},{"main/loss":0.0464901365339756,"validation/main/loss":0.06954242289066315,"iteration":900,"elapsed_time":16.742995977401733,"epoch":3,"main/accuracy":0.9852502346038818,"validation/main/accuracy":0.9788001179695129},{"main/loss":0.032701507210731506,"validation/main/loss":0.07573027163743973,"iteration":1200,"elapsed_time":18.258733987808228,"epoch":4,"main/accuracy":0.9894164204597473,"validation/main/accuracy":0.9782000780105591},{"main/loss":0.027782348915934563,"validation/main/loss":0.0726533755660057,"iteration":1500,"elapsed_time":19.855143070220947,"epoch":5,"main/accuracy":0.9907165765762329,"validation/main/accuracy":0.9786000847816467},{"main/loss":0.01710054837167263,"validation/main/loss":0.07857353240251541,"iteration":1800,"elapsed_time":21.436523914337158,"epoch":6,"main/accuracy":0.9945824146270752,"validation/main/accuracy":0.9794000387191772},{"main/loss":0.01630624383687973,"validation/main/loss":0.09265504032373428,"iteration":2100,"elapsed_time":22.991225004196167,"epoch":7,"main/accuracy":0.9945657253265381,"validation/main/accuracy":0.9763000011444092},{"main/loss":0.013817841187119484,"validation/main/loss":0.088636614382267,"iteration":2400,"elapsed_time":24.812855005264282,"epoch":8,"main/accuracy":0.9955657124519348,"validation/main/accuracy":0.9785000681877136},{"main/loss":0.013849375769495964,"validation/main/loss":0.07907723635435104,"iteration":2700,"elapsed_time":26.343821048736572,"epoch":9,"main/accuracy":0.9954158663749695,"validation/main/accuracy":0.9799001216888428},{"main/loss":0.01355580985546112,"validation/main/loss":0.0880671888589859,"iteration":3000,"elapsed_time":27.869792938232422,"epoch":10,"main/accuracy":0.9954991936683655,"validation/main/accuracy":0.9786998629570007},{"main/loss":0.014018351212143898,"validation/main/loss":0.10556967556476593,"iteration":3300,"elapsed_time":29.38447093963623,"epoch":11,"main/accuracy":0.9956490993499756,"validation/main/accuracy":0.9749000668525696},{"main/loss":0.006923248991370201,"validation/main/loss":0.10161171108484268,"iteration":3600,"elapsed_time":30.89717698097229,"epoch":12,"main/accuracy":0.997815728187561,"validation/main/accuracy":0.9778000712394714},{"main/loss":0.013207540847361088,"validation/main/loss":0.08085791766643524,"iteration":3900,"elapsed_time":32.47591686248779,"epoch":13,"main/accuracy":0.995749294757843,"validation/main/accuracy":0.9808000326156616},{"main/loss":0.009158046916127205,"validation/main/loss":0.08429741859436035,"iteration":4200,"elapsed_time":33.98557496070862,"epoch":14,"main/accuracy":0.9969495534896851,"validation/main/accuracy":0.9815000295639038},{"main/loss":0.010037709027528763,"validation/main/loss":0.08136351406574249,"iteration":4500,"elapsed_time":35.561367988586426,"epoch":15,"main/accuracy":0.9967491626739502,"validation/main/accuracy":0.9826000928878784},{"main/loss":0.008573469705879688,"validation/main/loss":0.08259663730859756,"iteration":4800,"elapsed_time":37.11731696128845,"epoch":16,"main/accuracy":0.9974660277366638,"validation/main/accuracy":0.9820000529289246},{"main/loss":0.010515258647501469,"validation/main/loss":0.09271233528852463,"iteration":5100,"elapsed_time":38.68516993522644,"epoch":17,"main/accuracy":0.9966659545898438,"validation/main/accuracy":0.9801999926567078},{"main/loss":0.00526642007753253,"validation/main/loss":0.07438076287508011,"iteration":5400,"elapsed_time":40.385915994644165,"epoch":18,"main/accuracy":0.9982661008834839,"validation/main/accuracy":0.9841001033782959},{"main/loss":0.0021944462787359953,"validation/main/loss":0.07695779204368591,"iteration":5700,"elapsed_time":41.93238306045532,"epoch":19,"main/accuracy":0.999433159828186,"validation/main/accuracy":0.9845000505447388},{"main/loss":0.005694549530744553,"validation/main/loss":0.10526148974895477,"iteration":6000,"elapsed_time":43.58621597290039,"epoch":20,"main/accuracy":0.9980993866920471,"validation/main/accuracy":0.9791998863220215}],"name":"/mnt/c/Development/gopath/src/github.com/chainer/chainerui/examples/example_results/19204"},"131":{"log":[{"main/loss":0.21457478404045105,"validation/main/loss":0.14474090933799744,"iteration":12000,"elapsed_time":50.188390016555786,"epoch":1,"main/accuracy":0.9371951222419739,"validation/main/accuracy":0.9595014452934265},{"main/loss":0.12027910351753235,"validation/main/loss":0.09368199855089188,"iteration":24000,"elapsed_time":88.79813814163208,"epoch":2,"main/accuracy":0.9672335386276245,"validation/main/accuracy":0.9723011255264282},{"main/loss":0.09617628902196884,"validation/main/loss":0.10325329750776291,"iteration":36000,"elapsed_time":127.78439116477966,"epoch":3,"main/accuracy":0.9744196534156799,"validation/main/accuracy":0.9741010069847107},{"main/loss":0.08207269757986069,"validation/main/loss":0.10191778093576431,"iteration":48000,"elapsed_time":167.09505009651184,"epoch":4,"main/accuracy":0.9789883494377136,"validation/main/accuracy":0.9747012257575989},{"main/loss":0.07095364481210709,"validation/main/loss":0.09880106151103973,"iteration":60000,"elapsed_time":205.54000306129456,"epoch":5,"main/accuracy":0.9826900959014893,"validation/main/accuracy":0.9741007685661316},{"main/loss":0.07125166058540344,"validation/main/loss":0.15311692655086517,"iteration":72000,"elapsed_time":246.8161461353302,"epoch":6,"main/accuracy":0.9833235144615173,"validation/main/accuracy":0.9718008637428284},{"main/loss":0.06143014132976532,"validation/main/loss":0.1492302566766739,"iteration":84000,"elapsed_time":286.32494497299194,"epoch":7,"main/accuracy":0.9855415225028992,"validation/main/accuracy":0.9754007458686829},{"main/loss":0.058628279715776443,"validation/main/loss":0.14753711223602295,"iteration":96000,"elapsed_time":326.53162717819214,"epoch":8,"main/accuracy":0.986642062664032,"validation/main/accuracy":0.9739008545875549},{"main/loss":0.05068863928318024,"validation/main/loss":0.2057991921901703,"iteration":108000,"elapsed_time":368.1037480831146,"epoch":9,"main/accuracy":0.9879096746444702,"validation/main/accuracy":0.9757007956504822},{"main/loss":0.05316668748855591,"validation/main/loss":0.17766107618808746,"iteration":120000,"elapsed_time":408.26054215431213,"epoch":10,"main/accuracy":0.9886595606803894,"validation/main/accuracy":0.9767005443572998},{"main/loss":0.04927712678909302,"validation/main/loss":0.19662946462631226,"iteration":132000,"elapsed_time":448.8655571937561,"epoch":11,"main/accuracy":0.989793598651886,"validation/main/accuracy":0.97500079870224},{"main/loss":0.05134021118283272,"validation/main/loss":0.19726237654685974,"iteration":144000,"elapsed_time":488.6945741176605,"epoch":12,"main/accuracy":0.9895272850990295,"validation/main/accuracy":0.9792007803916931},{"main/loss":0.048185065388679504,"validation/main/loss":0.2104976326227188,"iteration":156000,"elapsed_time":526.9440050125122,"epoch":13,"main/accuracy":0.9905443787574768,"validation/main/accuracy":0.975400447845459},{"main/loss":0.04741118848323822,"validation/main/loss":0.2823873460292816,"iteration":168000,"elapsed_time":568.7579929828644,"epoch":14,"main/accuracy":0.9907440543174744,"validation/main/accuracy":0.9760004878044128},{"main/loss":0.04370129853487015,"validation/main/loss":0.32624733448028564,"iteration":180000,"elapsed_time":609.3689150810242,"epoch":15,"main/accuracy":0.9918616414070129,"validation/main/accuracy":0.9738010168075562},{"main/loss":0.0460854135453701,"validation/main/loss":0.29909634590148926,"iteration":192000,"elapsed_time":649.0241661071777,"epoch":16,"main/accuracy":0.9918451309204102,"validation/main/accuracy":0.9769008755683899},{"main/loss":0.039479710161685944,"validation/main/loss":0.347767174243927,"iteration":204000,"elapsed_time":688.4191510677338,"epoch":17,"main/accuracy":0.9928626418113708,"validation/main/accuracy":0.976900577545166},{"main/loss":0.041237954050302505,"validation/main/loss":0.3420376479625702,"iteration":216000,"elapsed_time":726.8540260791779,"epoch":18,"main/accuracy":0.9918621182441711,"validation/main/accuracy":0.9746008515357971},{"main/loss":0.042271312326192856,"validation/main/loss":0.4085622727870941,"iteration":228000,"elapsed_time":765.0877981185913,"epoch":19,"main/accuracy":0.9928123354911804,"validation/main/accuracy":0.9766004681587219},{"main/loss":0.03995363414287567,"validation/main/loss":0.3028023838996887,"iteration":240000,"elapsed_time":803.4009599685669,"epoch":20,"main/accuracy":0.9931627511978149,"validation/main/accuracy":0.9772008061408997}],"name":"/mnt/c/Development/gopath/src/github.com/chainer/chainerui/examples/example_results/19205"},"132":{"log":[{"main/loss":0.1903551071882248,"validation/main/loss":0.08968492597341537,"iteration":600,"elapsed_time":13.695358037948608,"epoch":1,"main/accuracy":0.9425005912780762,"validation/main/accuracy":0.9721997976303101},{"main/loss":0.070682592689991,"validation/main/loss":0.07078154385089874,"iteration":1200,"elapsed_time":16.396203994750977,"epoch":2,"main/accuracy":0.9775658249855042,"validation/main/accuracy":0.978300154209137},{"main/loss":0.049275245517492294,"validation/main/loss":0.08069691061973572,"iteration":1800,"elapsed_time":19.07902193069458,"epoch":3,"main/accuracy":0.9838988184928894,"validation/main/accuracy":0.977100133895874},{"main/loss":0.03708365559577942,"validation/main/loss":0.08538221567869186,"iteration":2400,"elapsed_time":21.885788917541504,"epoch":4,"main/accuracy":0.9877811670303345,"validation/main/accuracy":0.9761000871658325},{"main/loss":0.02807035483419895,"validation/main/loss":0.0896487608551979,"iteration":3000,"elapsed_time":24.47069501876831,"epoch":5,"main/accuracy":0.9909316897392273,"validation/main/accuracy":0.974799633026123},{"main/loss":0.021846162155270576,"validation/main/loss":0.0743316113948822,"iteration":3600,"elapsed_time":27.149954080581665,"epoch":6,"main/accuracy":0.9925153851509094,"validation/main/accuracy":0.98089998960495},{"main/loss":0.019545959308743477,"validation/main/loss":0.07979840040206909,"iteration":4200,"elapsed_time":29.678422927856445,"epoch":7,"main/accuracy":0.9933819770812988,"validation/main/accuracy":0.979600191116333},{"main/loss":0.018406331539154053,"validation/main/loss":0.10919147729873657,"iteration":4800,"elapsed_time":32.20383906364441,"epoch":8,"main/accuracy":0.9939153790473938,"validation/main/accuracy":0.976599931716919},{"main/loss":0.017558660358190536,"validation/main/loss":0.08197624236345291,"iteration":5400,"elapsed_time":34.84123206138611,"epoch":9,"main/accuracy":0.9942818284034729,"validation/main/accuracy":0.9790999889373779},{"main/loss":0.01588689722120762,"validation/main/loss":0.08992187678813934,"iteration":6000,"elapsed_time":37.52797889709473,"epoch":10,"main/accuracy":0.9948152899742126,"validation/main/accuracy":0.9788002967834473}],"name":"/mnt/c/Development/gopath/src/github.com/chainer/chainerui/examples/example_results/19208"}},"config":{"xAxis":"epoch","yLeftAxis":["main/loss"],"yRightAxis":["main/accuracy"],"resultIds":[128,129,130,131,132]}}
"""


def _get_simple_logs():
    logs = {
        'data': {
            '1': {
                'name': 'first',
                'log': [
                    {
                        'loss': 0.1,
                        'loss2': 0.11,
                        'accuracy': 0.75,
                        'epoch': 1,
                        'iteration': 100
                    },
                    {
                        'loss': 0.01,
                        'loss2': 0.011,
                        'accuracy': 0.9,
                        'epoch': 2,
                        'iteration': 200
                    },
                ]
            },
            '2': {
                'name': 'long-long-long-long-long-second',
                'log': [
                    {
                        'loss': 0.15,
                        'loss2': 0.16,
                        'accuracy': 0.70,
                        'epoch': 1,
                        'iteration': 100
                    },
                    {
                        'loss': 0.015,
                        'loss2': 0.016,
                        'accuracy': 0.95,
                        'epoch': 2,
                        'iteration': 200
                    },
                ]
            }
        },
    }
    return logs


def _get_render_module(script_path, module_name):
    if sys.version_info.major == 2:
        import imp
        return imp.load_source(module_name, script_path)

    import importlib.util
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    render = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(render)
    return render


def _run_on_tempd(dir, f, *args, **kwargs):
    cwd = os.getcwd()
    try:
        os.chdir(dir)
        f(*args, **kwargs)
    finally:
        os.chdir(cwd)


@unittest.skipUnless(_check_flake8(), 'flake8 is not installed')
def test_script_format(func_dir):
    script_path = _get_script_path(func_dir, _get_example_logs())
    res = subprocess.call(['flake8', script_path])
    assert res == 0


def test_download(func_dir):
    script_path = _get_script_path(func_dir, _get_example_logs())
    render = _get_render_module(script_path, 'test_download')

    assert render.download().strip() == _get_example_logs().strip()


@unittest.skipUnless(_check_matplotlib(), 'matplotlib is not installed')
def test_render_main(func_dir):
    script_path = _get_script_path(func_dir, _get_example_logs())
    render = _get_render_module(script_path, 'test_render_main')

    _run_on_tempd(func_dir, render.main)

    assert os.path.exists(os.path.join(func_dir, 'log_chart.png'))


@unittest.skipUnless(_check_matplotlib(), 'matplotlib is not installed')
def test_render_both_axis(func_dir):
    script_path = _get_script_path(func_dir, '{}')  # dummy log data, not used
    render = _get_render_module(script_path, 'test_render_both_axis')

    logs = _get_simple_logs()
    both_config = {
        'xAxis': 'epoch',
        'yLeftAxis': ['loss', 'loss2'],
        'yRightAxis': ['accuracy'],
        'resultIds': [1, 2]
    }
    logs['config'] = both_config
    _run_on_tempd(func_dir, render.render, logs)

    assert os.path.exists(os.path.join(func_dir, 'log_chart.png'))


@unittest.skipUnless(_check_matplotlib(), 'matplotlib is not installed')
def test_render_right(func_dir):
    script_path = _get_script_path(func_dir, '{}')  # dummy log data, not used
    render = _get_render_module(script_path, 'test_render_both_axis')

    logs = _get_simple_logs()
    both_config = {
        'xAxis': 'epoch',
        'yLeftAxis': [],
        'yRightAxis': ['accuracy'],
        'resultIds': [1, 2]
    }
    logs['config'] = both_config
    _run_on_tempd(func_dir, render.render, logs)

    assert os.path.exists(os.path.join(func_dir, 'log_chart.png'))


@unittest.skipUnless(_check_matplotlib(), 'matplotlib is not installed')
def test_render_left(func_dir):
    script_path = _get_script_path(func_dir, '{}')  # dummy log data, not used
    render = _get_render_module(script_path, 'test_render_both_axis')

    logs = _get_simple_logs()
    both_config = {
        'xAxis': 'epoch',
        'yLeftAxis': ['loss', 'loss2'],
        'yRightAxis': [],
        'resultIds': [1, 2]
    }
    logs['config'] = both_config
    _run_on_tempd(func_dir, render.render, logs)

    assert os.path.exists(os.path.join(func_dir, 'log_chart.png'))


@unittest.skipUnless(_check_matplotlib(), 'matplotlib is not installed')
def test_render_empty(func_dir):
    script_path = _get_script_path(func_dir, '{}')  # dummy log data, not used
    render = _get_render_module(script_path, 'test_render_both_axis')

    logs = _get_simple_logs()
    configs = [
        {
            'xAxis': '',
            'yLeftAxis': ['loss', 'loss2'],
            'yRightAxis': ['accuracy'],
            'resultIds': [1, 2],
            'title': 'no selected x axis'
        },
        {
            'xAxis': 'step',
            'yLeftAxis': ['loss', 'loss2'],
            'yRightAxis': ['accuracy'],
            'resultIds': [1, 2],
            'title': 'invalid x-axis'
        },
        {
            'xAxis': 'epoch',
            'yLeftAxis': [],
            'yRightAxis': [],
            'resultIds': [1, 2],
            'title': 'no selected y values'
        },
        {
            'xAxis': 'epoch',
            'yLeftAxis': ['loss3'],
            'yRightAxis': [],
            'resultIds': [1, 2],
            'title': 'selected invalid y values'
        },
        {
            'xAxis': 'epoch',
            'yLeftAxis': ['loss', 'loss2'],
            'yRightAxis': ['accuracy'],
            'resultIds': [],
            'title': 'no selected results'
        },
        {
            'xAxis': 'epoch',
            'yLeftAxis': ['loss', 'loss2'],
            'yRightAxis': ['accuracy'],
            'resultIds': [3],
            'title': 'selected invalid result'
        }
    ]
    for config in configs:
        title = config.pop('title')
        logs['config'] = config
        _run_on_tempd(func_dir, render.render, logs)

        if os.path.exists(os.path.join(func_dir, 'log_chart.png')):
            pytest.fail('plot chart should not be created on {}'.format(title))
