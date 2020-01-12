function comp
    ovs=64;
    B=4;

    a=0.5*sin(2*pi*10000*linspace(0,1,44100*ovs));
    %aa=quant(a,B);
    b=DS_1(a,B);
    c=DS_2(a,B);
    d=DS_3(a,B);
    e=DS_4(a,B);
    f=DS_5(a,B);
    
    hold on;
    %pspectrum(aa,44100*ovs);
    pspectrum(b,44100*ovs);
    pspectrum(c,44100*ovs);
    pspectrum(d,44100*ovs);
    pspectrum(e,44100*ovs);
    pspectrum(f,44100*ovs);
    
    plot([22050e-6 22050e-6],[-120 0],'r')
    plot([0 22050e-6],[-120 -120],'r')
    legend('1','2','3','4','5');
    
    figure; plot(b);
    
    figure;
    hold on;
    %pspectrum(aa,44100*ovs,'FrequencyLimits',[0 22050],'FrequencyResolution',100);
    pspectrum(b,44100*ovs,'FrequencyLimits',[0 22050],'FrequencyResolution',100);
    pspectrum(c,44100*ovs,'FrequencyLimits',[0 22050],'FrequencyResolution',100);
    pspectrum(d,44100*ovs,'FrequencyLimits',[0 22050],'FrequencyResolution',100);
    pspectrum(e,44100*ovs,'FrequencyLimits',[0 22050],'FrequencyResolution',100);
    pspectrum(f,44100*ovs,'FrequencyLimits',[0 22050],'FrequencyResolution',100);
    
    plot([0 22050],[-120 -120],'r')
    legend('1','2','3','4','5');
    
    %audiowrite('1.wav',a,44100*ovs,'BitsPerSample',32);
    %audiowrite('2.wav',aa,44100*ovs,'BitsPerSample',32);
    %audiowrite('3.wav',b,44100*ovs,'BitsPerSample',32);
    %audiowrite('4.wav',c,44100*ovs,'BitsPerSample',32);
    %audiowrite('5.wav',d,44100*ovs,'BitsPerSample',32);
    %audiowrite('6.wav',e,44100*ovs,'BitsPerSample',32);
    %audiowrite('7.wav',f,44100*ovs,'BitsPerSample',32);
end