
import functools
import re
import numpy as np
import PIL.Image

_SEGMENT_DETECT_RE = re.compile(
    r'(.*?)' +
    r'<loc(\d{4})>' * 4 + r'\s*' +
    '(?:%s)?' % (r'<seg(\d{3})>' * 16) +
    r'\s*([^;<>]+)? ?(?:; )?',
)

def extract_objs(text, width, height, unique_labels=False):
  """Returns objs for a string with "<loc>" and "<seg>" tokens."""
  objs = []
  seen = set()
  while text:
    m = _SEGMENT_DETECT_RE.match(text)
    if not m:
      break

    gs = list(m.groups())
    before = gs.pop(0)
    name = gs.pop()
    y1, x1, y2, x2 = [int(x) / 1024 for x in gs[:4]]
    y1, x1, y2, x2 = map(round, (y1*height, x1*width, y2*height, x2*width))

    seg_indices = gs[4:20]
    if seg_indices[0] is None:
      mask = None
    else:
    #   seg_indices = np.array([int(x) for x in seg_indices], dtype=np.int32)
    #   m64, = _get_reconstruct_masks()(seg_indices[None])[..., 0]
    #   m64 = np.clip(np.array(m64) * 0.5 + 0.5, 0, 1)
    #   m64 = PIL.Image.fromarray((m64 * 255).astype('uint8'))
    #   mask = np.zeros([height, width])
    #   if y2 > y1 and x2 > x1:
    #     mask[y1:y2, x1:x2] = np.array(m64.resize([x2 - x1, y2 - y1])) / 255.0
        mask = None

    content = m.group()
    if before:
      objs.append(dict(content=before))
      content = content[len(before):]
    while unique_labels and name in seen:
      name = (name or '') + "'"
    seen.add(name)
    objs.append(dict(
        content=content, xyxy=(x1, y1, x2, y2), mask=mask, name=name))
    text = text[len(before) + len(content):]

  if text:
    objs.append(dict(content=text))

  return objs