// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © weknowLLC
//@version=5

indicator(title="50,100,150 SMA", shorttitle="SMA3", overlay=true, timeframe="", timeframe_gaps=true)
len = input.int(50, minval=1, title="Length")
len2 = input.int(100, minval=1, title="Length")
len3 = input.int(150, minval=1, title="Length")
src = input(close, title="Source")
offset = input.int(title="Offset", defval=0, minval=-500, maxval=500)

out = ta.ema(src, len)
out2 = ta.ema(src, len2)
out3 = ta.ema(src, len2)

plot(out, title="EMA50", color=color.blue, offset=offset)
plot(out2, title="EMA100", color=color.yellow, offset=offset)
plot(out3, title="EMA150", color=color.green, offset=offset)

ma(source, length, type) =>
    switch type
        "SMA" => ta.sma(source, length)
        "EMA" => ta.ema(source, length)
        "SMMA (RMA)" => ta.rma(source, length)
        "WMA" => ta.wma(source, length)
        "VWMA" => ta.vwma(source, length)

typeMA = input.string(title = "Method", defval = "SMA", options=["SMA", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="Smoothing")
smoothingLength = input.int(title = "Length", defval = 5, minval = 1, maxval = 100, group="Smoothing")

smoothingLine = ma(out, smoothingLength, typeMA)
plot(smoothingLine, title="Smoothing Line", color=#f37f20, offset=offset, display=display.none)
