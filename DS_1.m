function out=DS_1(in,B)
    x=0;
    for i=1:length(in)
        out(i)=quant(x,B);
        x=in(i)-out(i)+x;
    end
end