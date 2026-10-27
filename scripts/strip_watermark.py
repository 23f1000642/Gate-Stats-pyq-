import pikepdf, os
pdf=pikepdf.open(os.environ.get('PYQ_PDF','source/pyq.pdf'))
WM={(1280,25),(653,47),(2215,43),(2193,43)}
def clean(res, stream_owner):
    xo=res.get('/XObject',{})
    bad=set()
    for name,obj in xo.items():
        if obj.get('/Subtype')=='/Image' and (int(obj.Width),int(obj.Height)) in WM: bad.add(name)
        elif obj.get('/Subtype')=='/Form':
            clean(obj.get('/Resources',pikepdf.Dictionary()), obj)
    if bad:
        ops=pikepdf.parse_content_stream(stream_owner)
        new=[(o,op) for o,op in ops if not (str(op)=='Do' and str(o[0]) in bad)]
        data=pikepdf.unparse_content_stream(new)
        if isinstance(stream_owner,pikepdf.Page): stream_owner.obj.Contents=pdf.make_stream(data)
        else: stream_owner.write(data)
    return len(bad)
n=0
for pg in pdf.pages:
    n+=clean(pg.Resources,pg)
print('removed names',n)
pdf.save('build/clean.pdf')
