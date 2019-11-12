import ROOT as R 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, help="Input File")
parser.add_argument("--output", type=str, help="Output File")
args = parser.parse_args()

g = R.TGraphErrors(args.input)

func = R.TF1("wf", "pol1")
g.Fit("wf", "","", 2,70)

g.Draw("APL")

xs = []
ys = []
# estrapolate from 0 to 100
for x in range(0, 101):
    ys.append(func.Eval(x))
    xs.append(x)


with open(args.output, "w") as out:
    for x,y in zip(xs, ys):
        out.write("{:.0f} {}\n".format(x,y)) 


