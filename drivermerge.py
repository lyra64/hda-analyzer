from os import popen, mkdir, system, chdir, getcwd, remove, listdir
from os.path import isdir, exists, split
from utils import git_popen, git_system, git_repo, is_alsa_file, to_alsa_file2, \
def analyze_diff(fp, full=False, filter_git=False,
                 filecheck=is_alsa_file, fileconv=to_alsa_file2):

    def afile(file, prefix):
        if file.startswith('/dev/'):
            return file
        return prefix + file

    def hdr(rlines, addfiles, rmfiles, afile1, afile2):
      rlines.append('diff --git %s %s\n' % (afile(afile1, 'a/'), afile(afile2, 'b/')))
      rlines += hlines
      if hlines and (hlines[0].startswith('new file mode ') or \
         hlines[0].startswith('old mode ')):
        addfiles.append(afile2)
      elif hlines and hlines[0].startswith('deleted file mode '):
        rmfiles.append(afile1)

    hlines = []
    header = False
        if filter_git:
            if line.startswith('index ') and line.find('..') > 0:
                continue
            if line.startswith('new file mode '):
                continue
            if line.startswith('old mode '):
                continue
            if line.startswith('new mode '):
                continue
            if header and ok:
                hdr(rlines, addfiles, rmfiles, afile1, afile2)
            header = True
            hlines = []
            ok1 = filecheck(file1[2:])
            ok2 = filecheck(file2[2:])
                afile1 = fileconv(file1, 'a/')
                afile2 = fileconv(file2, 'b/')
        elif ok and line.startswith('--- /dev/null'):
            afile1 = line[4:].strip()
        elif ok and line.startswith('--- a/'):
            afile1 = fileconv(line[6:].strip())
        elif ok and line.startswith('+++ b/'):
            afile2 = fileconv(line[6:].strip())
            rlines.append('diff --git %s %s\n' % (afile1, afile2))
            rlines += hlines
            rlines.append('--- %s\n' % afile(afile1, 'a/'))
            rlines.append('+++ %s\n' % afile(afile2, 'b/'))
            addfiles.append(afile2)
            header = False
            rmfiles.append(afile1)
            rlines.append('diff --git %s %s\n' % (afile1, '/dev/null'))
            rlines += hlines
            rlines.append('--- %s\n' % afile(afile1, 'a/'))
            rlines.append('+++ /dev/null\n')
            header = False
        elif header:
            hlines.append(line)
    if header and ok:
        hdr(rlines, addfiles, rmfiles, afile1, afile2)
        src = git_repo(driver_repo) + '/' + to_alsa_file2(f)
        dst = git_repo(kernel_repo) + '/' + f
        lines = popen("diff -uN %s %s 2> /dev/null" % (src, dst)).readlines()
def try_to_merge(driver_repo, driver_branch, src_repo, commit,
                 filecheck=is_alsa_file, fileconv=to_alsa_file2,
                 do_checkout=True):
    #fp = git_popen(src_repo, "diff --binary %s~1..%s" % (ref, ref))
    root = ''
    if 'root_flag' in commit and commit['root_flag']:
      root = '--root '
    fp = git_popen(src_repo, "diff-tree -p --binary %s%s" % (root, ref))
    rlines, addfiles, rmfiles = analyze_diff(fp, filecheck=filecheck, fileconv=fileconv)
    patchfile = tmpfile('alsa-merge-patch')
    commentfile = tmpfile('alsa-merge-comment')
    if do_checkout and git_system(driver_repo, "checkout -q %s" % driver_branch):

    lines = popen("LANG=C patch -f -p 1 --dry-run --reject-file=%s < %s" % (tmpfile("rejects"), patchfile)).readlines()
    print ''.join(lines)
        if do_checkout and \
           ref[:7] in ['bdb527e', 'fc5b15f', '82b1d73', \
                       '02a237b', 'ef8d60f', 'c0fa6c8', \
                       '1605282', '3946860', 'd70f363', \
                       '6539799', '152a3a7', '79980d9']:
          print '  It is probably OK...'
          return False
        raise ValueError
    if git_system(driver_repo, "apply --check --binary --allow-binary-replacement %s" % patchfile):
        if not do_checkout:
          raise ValueError
    if git_system(driver_repo, "apply --binary --allow-binary-replacement %s" % patchfile):
    worktree = tmpdir('alsa-driver-repo')
    if git_system(driver_repo, "archive --format=tar %s mirror | tar xf - -C %s" % (driver_branch, worktree)):
        raise ValueError, 'git export (alsa-driver)'
    for f in listdir("alsa-kernel-repo/Documentation/DocBook"):
      if not f in ['.', '..', 'alsa-driver-api.tmpl']:
        x = "alsa-kernel-repo/Documentation/DocBook/" + f
        if isdir(x):
          rmtree(x)
        else:
          remove(x)
    remove("alsa-driver-repo/mirror/.gitignore")
    rmtree("alsa-driver-repo/mirror/scripts")
    rmtree("alsa-driver-repo/mirror/sound/oss")
    rmtree("alsa-kernel-repo/sound/oss")
    if 0:
      for i in ['.git-ok-commits', '.hgignore', '.hgtags', '.gitignore', 'kernel', 'scripts',
                'oss', 'usb/usbmixer.h', 'usb/usbmixer_maps.c']:
          if isdir("alsa-kmirror-repo/%s" % i):
              rmtree("alsa-kmirror-repo/%s" % i)
          elif exists("alsa-kmirror-repo/%s" % i):
              remove("alsa-kmirror-repo/%s" % i)
      for i in ['oss', 'pci/ac97/ak4531_codec.c', 'isa/sb/sb16_csp_codecs.h',
                'pci/korg1212/korg1212-firmware.h', 'pci/ymfpci/ymfpci_image.h',
                'pci/hda/hda_patch.h',
                'isa/ad1848/ad1848_lib.c', 'isa/cs423x/cs4231_lib.c', 'isa/cs423x/cs4232.c',
                'include/cs4231.h', 'soc/at91/eti_b1_wm8731.c',
                'aoa/codecs/snd-aoa-codec-onyx.c', 'aoa/codecs/snd-aoa-codec-onyx.h',
                'aoa/codecs/snd-aoa-codec-tas-basstreble.h', 'aoa/codecs/snd-aoa-codec-tas-gain-table.h',
                'aoa/codecs/snd-aoa-codec-tas.c', 'sound/aoa/codecs/snd-aoa-codec-tas.h',
                'aoa/codecs/snd-aoa-codec-toonie.c', 'aoa/core/snd-aoa-alsa.c',
                'aoa/core/snd-aoa-alsa.h', 'aoa/core/snd-aoa-core.c',
                'aoa/core/snd-aoa-gpio-feature.c', 'aoa/core/snd-aoa-gpio-pmf.c',
                'aoa/fabrics/snd-aoa-fabric-layout.c', 'aoa/soundbus/i2sbus/i2sbus-control.c',
                'aoa/soundbus/i2sbus/i2sbus-core.c', 'aoa/soundbus/i2sbus/i2sbus-interface.h',
                'aoa/soundbus/i2sbus/i2sbus-pcm.c', 'aoa/codecs/snd-aoa-codec-tas.h',
                'include/uda1341.h', 'i2c/l3/', 'arm/sa11xx-uda1341.c',
                'soc/at91/', 'soc/at32/', 'soc/s3c24xx/',
                'usb/caiaq/caiaq-audio.c', 'usb/caiaq/caiaq-audio.h',
                'usb/caiaq/caiaq-control.c', 'usb/caiaq/caiaq-control.h',
                'usb/caiaq/caiaq-device.c', 'usb/caiaq/caiaq-device.h',
                'usb/caiaq/caiaq-input.c', 'usb/caiaq/caiaq-input.h',
                'usb/caiaq/caiaq-midi.c', 'usb/caiaq/caiaq-midi.h',
                'usb/usbmixer.h',
                'usb/usbmixer_maps.c',
                'isa/wavefront/yss225.c'
                ]:
          if isdir("alsa-kernel-repo/%s" % i):
              rmtree("alsa-kernel-repo/%s" % i)
          elif exists("alsa-kernel-repo/%s" % i):
              remove("alsa-kernel-repo/%s" % i)
    fp = popen("diff -ruNp alsa-driver-repo/mirror alsa-kernel-repo")
    #kernel_commits = git_read_commits(kernel_repo, 'd80852223ecabd1ab433a9c71436d81b697ef1fc~1', 'd80852223ecabd1ab433a9c71436d81b697ef1fc', kernel_tree=True)