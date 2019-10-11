# Copyright 2019 Sonatype Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

from jake.parse.parse import Parse

oneCondaPackage = "alabaster                 0.7.12                   py27_0"

condaListOutput = '''# packages in environment at /anaconda2:
#
# Name                    Version                   Build  Channel
_ipyw_jlab_nb_ext_conf    0.1.0                    py27_0  
alabaster                 0.7.12                   py27_0  
anaconda-client           1.7.2                    py27_0  
anaconda-navigator        1.9.7                    py27_0  
anaconda-project          0.8.2                    py27_0  
appnope                   0.1.0            py27hb466136_0  
appscript                 1.1.0            py27h1de35cc_0  
asn1crypto                0.24.0                   py27_0  
astroid                   1.6.5                    py27_0  
atomicwrites              1.3.0                    py27_1  
attrs                     19.1.0                   py27_1  
babel                     2.6.0                    py27_0  
backports                 1.0                      py27_1  
backports.functools_lru_cache 1.5                      py27_1  
backports.os              0.1.1                    py27_0  
backports.shutil_get_terminal_size 1.0.0                    py27_2  
backports_abc             0.5              py27h6972548_0  
beautifulsoup4            4.7.1                    py27_1  
bitarray                  0.8.3            py27h1de35cc_0  
blas                      1.0                         mkl  
bleach                    3.1.0                    py27_0  
blosc                     1.15.0               hd9629dc_0  
boto                      2.49.0                   py27_0  
bzip2                     1.0.6                h1de35cc_5  
ca-certificates           2019.8.28                     0  
cairo                     1.14.12              hc4e6be7_4    http://localhost:8081/repository/conda-proxy/main
cdecimal                  2.3              py27h1de35cc_3  
certifi                   2019.9.11                py27_0  
cffi                      1.12.2           py27hb5b8e2f_1  
chardet                   3.0.4                    py27_1  
click                     7.0                      py27_0  
cloudpickle               0.8.0                    py27_0  
clyent                    1.2.2                    py27_1  
colorama                  0.4.1                    py27_0  
conda                     4.7.12                   py27_0  
conda-build               3.17.8                   py27_0  
conda-env                 2.6.0                         1  
conda-package-handling    1.6.0            py27h1de35cc_0  
conda-verify              3.1.1                    py27_0  
configparser              3.7.3                    py27_1  
contextlib2               0.5.5            py27h9cb85f4_0  
cryptography              2.6.1            py27ha12b0ac_0  
curl                      7.64.0               ha441bb4_2  
cycler                    0.10.0           py27hfc73c78_0  
cython                    0.29.6           py27h0a44026_0  
cytoolz                   0.9.0.1          py27h1de35cc_1  
dask-core                 1.1.4                    py27_1  
dbus                      1.13.6               h90a0687_0  
decorator                 4.4.0                    py27_1  
defusedxml                0.5.0                    py27_1  
distributed               1.26.0                   py27_1  
docutils                  0.14             py27h0befae3_0  
entrypoints               0.3                      py27_0  
enum34                    1.1.6                    py27_1  
et_xmlfile                1.0.1            py27hc42f929_0  
expat                     2.2.6                h0a44026_0  
fastcache                 1.0.2            py27h1de35cc_2  
filelock                  3.0.10                   py27_0  
flask                     1.0.2                    py27_1  
fontconfig                2.13.0               h5d5b041_1    http://localhost:8081/repository/conda-proxy/main
freetype                  2.9.1                hb4e5f40_0  
funcsigs                  1.0.2            py27hb9f6266_0  
functools32               3.2.3.2                  py27_1  
future                    0.17.1                   py27_0  
futures                   3.2.0                    py27_0  
get_terminal_size         1.0.0                h7520d66_0  
gettext                   0.19.8.1             h15daf44_3  
gevent                    1.4.0            py27h1de35cc_0  
glib                      2.56.2               hd9629dc_0  
glob2                     0.6                      py27_1  
gmp                       6.1.2                hb37e062_1  
gmpy2                     2.0.8            py27h6ef4df4_2  
greenlet                  0.4.15           py27h1de35cc_0  
grin                      1.2.1                    py27_4  
hdf5                      1.10.4               hfa1e0ec_0  
heapdict                  1.0.0                    py27_2  
html5lib                  1.0.1                    py27_0  
icu                       58.2                 h4b95b61_1  
idna                      2.8                      py27_0  
imagesize                 1.1.0                    py27_0  
importlib_metadata        0.8                      py27_0  
intel-openmp              2019.3                      199  
ipaddress                 1.0.22                   py27_0  
ipykernel                 4.10.0                   py27_0  
ipython                   5.8.0                    py27_0  
ipython_genutils          0.2.0            py27h8b9a179_0  
ipywidgets                7.4.2                    py27_0  
isort                     4.3.16                   py27_0  
itsdangerous              1.1.0                    py27_0  
jbig                      2.1                  h4d881f8_0  
jdcal                     1.4                      py27_0  
jedi                      0.13.3                   py27_0  
jinja2                    2.10                     py27_0  
jpeg                      9b                   he5867d9_2  
jsonschema                3.0.1                    py27_0  
jupyter                   1.0.0                    py27_7  
jupyter_client            5.2.4                    py27_0  
jupyter_console           5.2.0                    py27_1  
jupyter_core              4.4.0                    py27_0  
jupyterlab                0.33.11                  py27_0  
jupyterlab_launcher       0.11.2           py27h28b3542_0  
keyring                   18.0.0                   py27_0  
kiwisolver                1.0.1            py27h0a44026_0  
krb5                      1.16.1               hddcf347_7  
lazy-object-proxy         1.3.1            py27h1de35cc_2  
libarchive                3.3.3                h786848e_5  
libcurl                   7.64.0               h051b688_2  
libcxx                    4.0.1                hcfea43d_1  
libcxxabi                 4.0.1                hcfea43d_1  
libedit                   3.1.20181209         hb402a30_0  
libffi                    3.2.1                h475c297_4  
libgfortran               3.0.1                h93005f0_2  
libiconv                  1.15                 hdd342a3_7  
liblief                   0.9.0                h2a1bed3_2  
libpng                    1.6.36               ha441bb4_0  
libsodium                 1.0.16               h3efe00b_0  
libssh2                   1.8.0                ha12b0ac_4  
libtiff                   4.0.10               hcb84e12_2  
libxml2                   2.9.9                hab757c2_0  
libxslt                   1.1.33               h33a18ac_0  
linecache2                1.0.0                    py27_0  
llvmlite                  0.28.0           py27h8c7ce04_0  
locket                    0.2.0            py27ha10513d_1  
lxml                      4.3.2            py27hef8c89e_0  
lz4-c                     1.8.1.2              h1de35cc_0  
lzo                       2.10                 h362108e_2  
markupsafe                1.1.1            py27h1de35cc_0  
mccabe                    0.6.1                    py27_1  
mistune                   0.8.4            py27h1de35cc_0  
mkl                       2019.4                      233  
mkl-service               2.3.0            py27hfbe908c_0  
mkl_fft                   1.0.12           py27h5e564d8_0    http://localhost:8081/repository/conda-proxy/main
mkl_random                1.0.2            py27h27c97d8_0  
more-itertools            5.0.0                    py27_0  
mpc                       1.1.0                h6ef4df4_1  
mpfr                      4.0.1                h3018a27_3  
mpmath                    1.1.0                    py27_0  
msgpack-python            0.6.1            py27h04f5b5a_1  
multipledispatch          0.6.0                    py27_0  
navigator-updater         0.2.1                    py27_0  
nbconvert                 5.4.1                    py27_3  
nbformat                  4.4.0            py27hddc86d0_0  
ncurses                   6.1                  h0a44026_1  
networkx                  2.2                      py27_1  
nltk                      3.4                      py27_1  
nose                      1.3.7                    py27_2  
notebook                  5.7.8                    py27_0  
numpy                     1.16.5           py27hacdab7b_0  
numpy-base                1.16.5           py27h6575580_0  
numpydoc                  0.8.0                    py27_0  
olefile                   0.46                     py27_0  
openpyxl                  2.6.1                    py27_1  
openssl                   1.1.1d               h1de35cc_2  
packaging                 19.0                     py27_0  
pandoc                    2.2.3.2                       0  
pandocfilters             1.4.2                    py27_1  
parso                     0.3.4                    py27_0  
partd                     0.3.10                   py27_1  
path.py                   11.5.0                   py27_0  
pathlib2                  2.3.3                    py27_0  
pcre                      8.43                 h0a44026_0  
pep8                      1.7.1                    py27_0  
pexpect                   4.6.0                    py27_0  
pickleshare               0.7.5                    py27_0  
pillow                    5.4.1            py27hb68e598_0  
pip                       19.0.3                   py27_0  
pixman                    0.38.0               h1de35cc_0    http://localhost:8081/repository/conda-proxy/main
pkginfo                   1.5.0.1                  py27_0  
pluggy                    0.9.0                    py27_0  
ply                       3.11                     py27_0  
portaudio                 19.6.0               h41429eb_1  
prometheus_client         0.6.0                    py27_0  
prompt_toolkit            1.0.15           py27h4a7b9c2_0  
psutil                    5.6.1            py27h1de35cc_0  
ptyprocess                0.6.0                    py27_0  
py                        1.8.0                    py27_0  
py-lief                   0.9.0            py27h1413db1_2  
pyaudio                   0.2.11           py27h1de35cc_1  
pycodestyle               2.5.0                    py27_0  
pycosat                   0.6.3            py27h1de35cc_0  
pycparser                 2.19                     py27_0  
pycrypto                  2.6.1            py27h1de35cc_9  
pycurl                    7.43.0.2         py27ha12b0ac_0  
pyflakes                  2.1.1                    py27_0  
pygments                  2.3.1                    py27_0  
pylint                    1.9.2                    py27_0  
pyodbc                    4.0.26           py27h0a44026_0  
pyopenssl                 19.0.0                   py27_0  
pyparsing                 2.3.1                    py27_0  
pyqt                      5.9.2            py27h655552a_2  
pyrsistent                0.14.11          py27h1de35cc_0  
pysocks                   1.6.8                    py27_0  
pytest                    4.3.1                    py27_0  
python                    2.7.16               h97142e2_0  
python-dateutil           2.8.0                    py27_0  
python-libarchive-c       2.8                      py27_6  
python.app                2                        py27_9  
pytz                      2018.9                   py27_0  
pyyaml                    5.1              py27h1de35cc_0  
pyzmq                     18.0.0           py27h0a44026_0  
qt                        5.9.7                h468cd18_1  
qtawesome                 0.5.7                    py27_1  
qtconsole                 4.4.3                    py27_0  
qtpy                      1.7.0                    py27_1  
readline                  7.0                  h1de35cc_5  
requests                  2.21.0                   py27_0  
rope                      0.12.0                   py27_0  
ruamel_yaml               0.15.46          py27h1de35cc_0  
scandir                   1.10.0           py27h1de35cc_0  
send2trash                1.5.0                    py27_0  
setuptools                40.8.0                   py27_0  
simplegeneric             0.8.1                    py27_2  
singledispatch            3.4.0.3          py27he22c18d_0  
sip                       4.19.8           py27h0a44026_0  
six                       1.12.0                   py27_0  
snappy                    1.1.7                he62c110_3  
snowballstemmer           1.2.1            py27h68ac032_0  
sortedcollections         1.1.2                    py27_0  
sortedcontainers          2.1.0                    py27_0  
soupsieve                 1.8                      py27_0  
sphinx                    1.8.5                    py27_0  
sphinxcontrib             1.0                      py27_1  
sphinxcontrib-websupport  1.1.0                    py27_1  
spyder                    3.3.3                    py27_0  
spyder-kernels            0.4.2                    py27_0  
sqlalchemy                1.3.1            py27h1de35cc_0  
sqlite                    3.27.2               ha441bb4_0  
ssl_match_hostname        3.7.0.1                  py27_0  
subprocess32              3.5.3            py27h1de35cc_0  
sympy                     1.3                      py27_0  
tblib                     1.3.2            py27ha684fc4_0  
terminado                 0.8.1                    py27_1  
testpath                  0.4.2                    py27_0  
tk                        8.6.8                ha441bb4_0  
toolz                     0.9.0                    py27_0  
tornado                   5.1.1            py27h1de35cc_0  
tqdm                      4.31.1                   py27_1  
traceback2                1.4.0                    py27_0  
traitlets                 4.3.2            py27hcf08151_0  
typing                    3.6.6                    py27_0  
unicodecsv                0.14.1           py27h170f95c_0  
unittest2                 1.1.0                    py27_0  
unixodbc                  2.3.7                h1de35cc_0  
urllib3                   1.24.1                   py27_0  
wcwidth                   0.1.7            py27h817c265_0  
webencodings              0.5.1                    py27_1  
werkzeug                  0.14.1                   py27_0  
wheel                     0.33.1                   py27_0  
widgetsnbextension        3.4.2                    py27_0  
wrapt                     1.11.1           py27h1de35cc_0  
wurlitzer                 1.0.2                    py27_0  
xlrd                      1.2.0                    py27_0  
xlsxwriter                1.1.5                    py27_0  
xlwings                   0.15.4                   py27_0  
xlwt                      1.2.0            py27hbeec4ae_0  
xz                        5.2.4                h1de35cc_4  
yaml                      0.1.7                hc338f04_2  
zeromq                    4.3.1                h0a44026_3  
zict                      0.1.4                    py27_0  
zipp                      0.3.3                    py27_1  
zlib                      1.2.11               h1de35cc_3  
zstd                      1.3.7                h5bba6e5_0'''

class TestParse(unittest.TestCase):
    def setUp(self):
        self.func = Parse()

    def test_callGetDependenciesReturnsPurls(self):
        actual = self.func.getDependencies(run_command_list=self.mockListCommand())
        self.assertEqual(actual, '{"coordinates": ["pkg:conda/alabaster@0.7.12"]}')

    def mockListCommand(self):
        oneWithHeader = '''#
# Name                    Version                   Build  Channel
''' + oneCondaPackage
        return oneWithHeader, "", 0
